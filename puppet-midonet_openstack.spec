%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:                   puppet-midonet_openstack
Version:                1.0.0
Release:                1%{?dist}
Summary:                Define profiles and roles to deploy MidoNet with OpenStack
License:                ASL 2.0

URL:                    https://github.com/midonet/puppet-midonet_openstack

Source0:                https://github.com/midonet/puppet-midonet_openstack/archive/%{version}.tar.gz

BuildArch:              noarch

Requires:               puppet-stdlib
Requires:               puppet-java
Requires:               puppet-cassandra
Requires:               puppet-zookeeper

Requires:               puppet >= 2.7.0

%description
Define profiles and roles for deploy MidoNet with OpenStack

%prep
%setup -q -n %{name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/midonet_openstack/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/midonet_openstack/



%files
%{_datadir}/openstack-puppet/modules/midonet_openstack/


%changelog
