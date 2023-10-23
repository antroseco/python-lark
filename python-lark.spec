Name:           python-lark
Version:        1.1.8
Release:        %autorelease
Summary:        a modern parsing library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/lark-parser/lark
Source:         %{pypi_source lark}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'lark' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-lark
Summary:        %{summary}

%description -n python3-lark %_description


%prep
%autosetup -p1 -n lark-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import -t


%files -n python3-lark -f %{pyproject_files}


%changelog
%autochangelog