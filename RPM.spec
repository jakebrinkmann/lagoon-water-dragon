
# This spec file can be used to build an RPM package for installation.
# **NOTE**
#     Version, Release, and tagname information should be updated for the
#     particular release to build an RPM for.

# ----------------------------------------------------------------------------
Name:		espa-surface-water-extent
Version:	201512
Release:	1%{?dist}
Summary:	ESPA Surface Water Extent Software

Group:		ESPA
License:	Nasa Open Source Agreement
URL:		https://github.com/USGS-EROS/espa-surface-water-extent.git

BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	x86_64
Packager:	USGS EROS LSRD

BuildRequires:	espa-common
Requires:	espa-common >= 1.4.0


# ----------------------------------------------------------------------------
%description
Provides science application executables for generating surface water extent products.  These applications are implementated in C and are statically built.


# ----------------------------------------------------------------------------
# Specify the repository tag/branch to clone and build from
%define tagname dev_dec2015
# Specify the name of the directory to clone into
%define clonedname %{name}-%{tagname}


# ----------------------------------------------------------------------------
%prep
# We don't need to perform anything here


# ----------------------------------------------------------------------------
%build

# Start with a clean clone of the repo
rm -rf %{clonedname}
git clone --depth 1 --branch %{tagname} %{url} %{clonedname}
# Build the applications
cd %{clonedname}
make BUILD_STATIC=yes


# ----------------------------------------------------------------------------
%install
# Start with a clean installation location
rm -rf %{buildroot}
# Install the applications for a specific path
cd %{clonedname}
make install PREFIX=%{buildroot}/usr/local

# ----------------------------------------------------------------------------
%clean
# Cleanup our cloned repository
rm -rf %{clonedname}
# Cleanup our installation location
rm -rf %{buildroot}


# ----------------------------------------------------------------------------
%files
%defattr(-,root,root,-)
# All sub-directories are automatically included
/usr/local/bin/*
/usr/local/%{name}


# ----------------------------------------------------------------------------
%changelog
* Tue Oct 27 2015 Ronald D Dilley <rdilley@usgs.gov>
- Updated RPM spec for Dec 2015 release

* Fri Sep 11 2015 William D Howe <whowe@usgs.gov>
- Rebuild for espa-common 1.5.0 version
* Fri Jun 26 2015 William D Howe <whowe@usgs.gov>
- Uses git hub now, cleaned up comments
* Thu May 22 2015 Cory B Turner <cbturner@usgs.gov>
- Rebuild to 1.0.3 for May 2015 release
* Tue Mar 31 2015 Adam J Dosch <adosch@usgs.gov>
- Version 1.0.2 release to ops
* Tue Mar 10 2015 Adam J Dosch <adosch@usgs.gov>
- John Jones changes incorporated for algorithm adjustments.  Hotfix release, rebuild to 1.0.1
* Tue Mar 03 2015 Adam J Dosch <adosch@usgs.gov>
- Minor modifications to code per John Jones to be included in March 2015 release, rebuild of same version with changes
* Tue Feb 10 2015 Adam J Dosch <adosch@usgs.gov>
- Minor build mods to spec file to get DSWE build working for March 2015 release
* Thu Jan 29 2015 Adam J Dosch <adosch@usgs.gov>
- Rebuilding swe code to put into production for March 2014 release
- Obsoleting swe pkg name and renaming to dswe
* Thu Aug 21 2014 Adam J Dosch <adosch@usgs.gov>
- Updated Release conditional macro to expand if exists, if non-exists must be broke?
* Fri Jul 18 2014 Adam J Dosch <adosch@usgs.gov>
- Merging RHEL5 and 6 changes together to maintain one spec file
* Thu Nov 07 2013 Adam J Dosch <adosch@usgs.gov>
- Updating cots paths from /data/static-cots to /data/cots
* Wed Nov 06 2013 Adam J Dosch <adosch@usgs.gov>
- Rebuild for version 0.0.1 for November 2013 release
- Updating SVN repository to build from Google code repo vs local SVN repo
* Mon Aug 07 2013 Adam J Dosch <adosch@usgs.gov>
- Hacked together RPM to package SWE into RPM form
  NOTE: Make sure the binary packages of 