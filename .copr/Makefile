.PHONY: srpm
srpm:
	dnf -y install rpm-build rpmdevtools
	spectool -g $(spec)
	rpmbuild -bs $(spec) --define "_srcrpmdir $(outdir)"
