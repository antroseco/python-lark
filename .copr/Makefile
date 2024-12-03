.PHONY: srpm
srpm:
	dnf -y install rpkg
	rpkg sources --outdir $(outdir)
	rpkg srpm --outdir $(outdir) --spec $(spec)
