#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <sys/stat.h>
#include <stdio.h>
#include <stdlib.h>
#include <pwd.h>
#include <grp.h>
#include <sys/file.h>
#include <errno.h>


#define MENU_DIR "/var/lib/menu"
#define KDE_MENU_DIR MENU_DIR"/kde"
#define USER_NAME "djurban"

char **env = { 0 };

/* Drop root privileges */
void droproot(const char *username)
{
  struct passwd *pw = NULL;
  pw = getpwnam( username );
  if ( pw ) {
    if ( initgroups(pw->pw_name, 0) != 0 || setgid(pw->pw_gid) != 0 ||
	 setuid(pw->pw_uid) != 0 ) {
      fprintf(stderr, "Couldn't change to '%.32s' uid=%d gid=%d\n", username, 
	      pw->pw_uid, pw->pw_gid);
      exit(1);
    }
  }
  else {
    fprintf(stderr, "Couldn't find user '%.32s'\n", username);
    exit(1);
  }
}


static int lockfile_fd = 0;
const char *lockfile_path=KDE_MENU_DIR ".lck";

void unlock_file()
{
  if (lockfile_fd) {
    flock(lockfile_fd, LOCK_UN);
    close(lockfile_fd);
  }
  if (lockfile_path)
    unlink(lockfile_path);	  
}

void lock_file()
{
  lockfile_fd = open(lockfile_path, O_CREAT|O_RDONLY, 0600);

  if (lockfile_fd == -1) {
    fprintf(stderr, "cannot open %s!\n", lockfile_path);
    perror("open");
    exit(10);
  }

  if (flock(lockfile_fd, LOCK_EX|LOCK_NB)) {
    if(errno == EAGAIN)
      fprintf(stderr, "desktop-create-kmenu is already running!\n");
    else
      perror("flock");
    exit(10);
  }
}

int main(int argc, char **argv)
{
  pid_t pid;
  struct passwd *pw = NULL;
  struct stat buf;

  chdir("/");

  pw = getpwnam( USER_NAME );
  if(!pw) {
    perror("Couldn't find user "USER_NAME);
    exit(1);
  }     

  if (stat(MENU_DIR, &buf) != 0) {
    mkdir (MENU_DIR, 0755);
    if (stat(MENU_DIR, &buf) != 0) {
      perror("Couldn't not create directory "MENU_DIR);
      exit(1);    
    }
  }

  if (( buf.st_mode & 07777 ) != 0755) {
    if ( chmod (MENU_DIR, 0755) != 0 ) {
      perror("Couldn't chmod "MENU_DIR" to 0755");
      exit(1);
    }
  }

  if (buf.st_uid != pw->pw_uid || buf.st_gid != pw->pw_gid) {
    if (chown(MENU_DIR, pw->pw_uid, pw->pw_gid) != 0) {
      perror("Couldn't chown "MENU_DIR);
      exit(1);
    }
  }

  droproot(USER_NAME);

  atexit(unlock_file);

  lock_file();

  umask(0022);  

  if ((pid = fork()) == 0) {
    execle("/bin/rm", "rm", "-fr", 
	   KDE_MENU_DIR, NULL, env);
  }
  if (pid == -1) {
    perror("Unable to fork");
    exit(1);
  }
  waitpid(pid, 0, 0);

  if ((pid = fork()) == 0) {
    execle("/usr/bin/desktop-menu-tool", "desktop-menu-tool", 
	   "--dir=" KDE_MENU_DIR, "--desktop=KDE", 
	   "/etc/X11/desktop-menus/applications.menu", NULL, env);
  }
  if (pid == -1) {
    perror("Unable to fork");
    exit(1);
  }
  waitpid(pid, 0, 0);

  return 0;
}
