import os

def drop_privileges(username, groupname):
    try:
        target_uid = pwd.getpwnam(username).pw_uid
        target_gid = grp.getgrnam(groupname).gr_gid
        os.setegid(target_gid)
        os.seteuid(target_uid)
    except (KeyError, OSError) as e:
        print(f"Failed to drop privileges: {str(e)}")
