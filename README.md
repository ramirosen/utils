# General-Linux-Utils
General  Linux Bash Utils

Contributed by Rami Rosen
http://ramirose.wixsite.com/ramirosen


errno:  A script for fetching a description of errno.
        Sometimes you want to get immediately the errno description
        without grepping in the kernel code.
        With this script, all you need to do is run ./errno  errorNumber

	For example:
	./errno 22
	will return:
	EINVAL          22      /* Invalid argument */
