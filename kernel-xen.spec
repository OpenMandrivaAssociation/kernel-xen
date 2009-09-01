%define name                    kernel-xen
%define version                 2.6.30.2
%define rel                     1
%define kernel_version          2.6.30.2
%define kernel_extraversion     xen-%{rel}mdv
# ensures file uniqueness
%define kernel_file_string      %{kernel_version}-xen-%{rel}mdv
# ensures package uniqueness
%define kernel_package_string   %{kernel_version}-%{rel}mdv

%ifarch %ix86
%define config %{SOURCE1}
%endif
%ifarch x86_64
%define config %{SOURCE2}
%endif

Name:       %{name}
Version:    %{version}
Release:    %mkrel %{rel}
Summary:    The Xen kernel
Group:      System/Kernel and hardware
License:    GPL
Source0:    linux-%{version}.tar.bz2
Source1:    i386_defconfig-server
Source2:    x86_64_defconfig-server
Patch60000:	60000_add-console-use-vt.patch1
Patch60001:	60001_linux-2.6.19-rc1-kexec-move_segment_code-i386.patch1
Patch60002:	60002_linux-2.6.19-rc1-kexec-move_segment_code-x86_64.patch1
Patch60003:	60003_ipv6-no-autoconf.patch1
Patch60004:	60004_pci-guestdev.patch1
Patch60005:	60005_pci-reserve.patch1
Patch60006:	60006_sfc-driverlink.patch1
Patch60007:	60007_sfc-resource-driver.patch1
Patch60008:	60008_sfc-driverlink-conditional.patch1
Patch60009:	60009_sfc-external-sram.patch1
Patch60010:	60010_xen3-auto-xen-arch.patch1
Patch60011:	60011_xen3-auto-xen-drivers.patch1
Patch60012:	60012_xen3-auto-include-xen-interface.patch1
Patch60013:	60013_xen3-auto-xen-kconfig.patch1
Patch60014:	60014_xen3-auto-common.patch1
Patch60015:	60015_xen3-auto-arch-x86.patch1
Patch60016:	60016_xen3-auto-arch-i386.patch1
Patch60017:	60017_xen3-auto-arch-x86_64.patch1
Patch60018:	60018_xen3-fixup-xen.patch1
Patch60019:	60019_sfc-sync-headers.patch1
Patch60020:	60020_sfc-endianness.patch1
Patch60021:	60021_xen3-fixup-kconfig.patch1
Patch60022:	60022_xen3-fixup-common.patch
Patch60023:	60023_xen3-fixup-arch-x86.patch1
Patch60024:	60024_xen3-patch-2.6.18.patch1
Patch60025:	60025_xen3-patch-2.6.19.patch1
Patch60026:	60026_xen3-patch-2.6.20.patch1
Patch60027:	60027_xen3-patch-2.6.21.patch1
Patch60028:	60028_xen3-patch-2.6.22.patch1
Patch60029:	60029_xen3-patch-2.6.23.patch1
Patch60030:	60030_xen3-patch-2.6.24.patch1
Patch60031:	60031_xen3-patch-2.6.25.patch1
Patch60032:	60032_xen3-patch-2.6.26.patch1
Patch60033:	60033_xen3-patch-2.6.27.patch
Patch60034:	60034_xen3-patch-2.6.28.patch
Patch60035:	60035_xen3-patch-2.6.29.patch1
Patch60036:	60036_xen3-patch-2.6.30.patch1
Patch60037:	60037_xen-balloon-max-target.patch1
Patch60038:	60038_xen-blkback-cdrom.patch1
Patch60039:	60039_xen-blktap-write-barriers.patch1
Patch60040:	60040_xen-scsifront-block-timeout-update.patch1
Patch60041:	60041_xen-op-packet.patch1
Patch60042:	60042_xen-blkfront-cdrom.patch1
Patch60043:	60043_xen-sections.patch1
Patch60044:	60044_xen-kconfig-compat.patch1
Patch60045:	60045_xen-cpufreq-report.patch1
Patch60046:	60046_xen-staging-build.patch1
Patch60047:	60047_xen-sysdev-suspend.patch1
Patch60048:	60048_xen-ipi-per-cpu-irq.patch1
Patch60049:	60049_xen-virq-per-cpu-irq.patch1
Patch60050:	60050_xen-configurable-guest-devices.patch1
Patch60051:	60051_xen-netback-nr-irqs.patch1
Patch60052:	60052_xen-netback-notify-multi.patch1
Patch60053:	60053_xen-x86-panic-no-reboot.patch1
Patch60054:	60054_xen-x86-dcr-fallback.patch1
Patch60055:	60055_xen-x86-consistent-nmi.patch1
Patch60056:	60056_xen-x86-no-lapic.patch1
Patch60057:	60057_xen-x86-pmd-handling.patch1
Patch60058:	60058_xen-x86-bigmem.patch1
Patch60059:	60059_xen-x86-machphys-prediction.patch1
Patch60060:	60060_xen-x86-exit-mmap.patch1
Patch60061:	60061_xen-x86_64-pgd-pin.patch1
Patch60062:	60062_xen-x86_64-pgd-alloc-order.patch1
Patch60063:	60063_xen-x86_64-dump-user-pgt.patch1
Patch60064:	60064_xen-x86_64-note-init-p2m.patch1
Patch60065:	60065_xen-x86-blktap2-nosmp.patch1
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description 
The XEN kernel.

%package -n kernel-xen-%{kernel_package_string}
Version:    1
Release:    %mkrel 1
Summary:    XEN kernel
Group:      System/Kernel and hardware
Provides:   kernel = %{kernel_version}
Provides:   kernel-xen = %{kernel_version}

%description -n kernel-xen-%{kernel_package_string}
The XEN kernel.

%package -n kernel-xen-devel-%{kernel_package_string}
Version:    1
Release:    %mkrel 1
Summary:    XEN kernel sources
Group:      System/Kernel and hardware
Requires:   kernel-xen-%{kernel_package_string}
Provides:   kernel-devel = %{kernel_version}

%description -n kernel-xen-devel-%{kernel_package_string}
XEN kernel sources.

%package -n kernel-xen-debug-%{kernel_package_string}
Version:  1
Release:  %mkrel 1
Summary:  Xen kernel debug files
Group:    Development/Debug
Requires: glibc-devel
Provides: kernel-debug = %{kernel_version}
Autoreqprov: no

%description -n kernel-xen-debug-%{kernel_package_string}
This package contains the kernel-debug files that should be enough to 
use debugging/monitoring tool (like systemtap, oprofile, ...)

%prep
%setup -q -n linux-%{kernel_version}
%apply_patches
perl -pi -e 's/EXTRAVERSION = (.*)/EXTRAVERSION = $1-%{kernel_extraversion}/' \
    Makefile

%build
cp -f %config .config
%make prepare 
%make
%make modules

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/boot
%make install INSTALL_PATH=%{buildroot}/boot
%make modules_install INSTALL_MOD_PATH=%{buildroot}

# have versionned files in /boot
mv %{buildroot}/boot/vmlinuz %{buildroot}/boot/vmlinuz-%{kernel_file_string}
mv %{buildroot}/boot/System.map %{buildroot}/boot/System.map-%{kernel_file_string}
install -m 644 .config %{buildroot}/boot/config-%{kernel_file_string}

# remove firmwares
rm -rf %{buildroot}/lib/firmware

# remove symlinks
rm -f %{buildroot}/lib/modules/%{kernel_file_string}/build
rm -f %{buildroot}/lib/modules/%{kernel_file_string}/source

# strip modules, as spec-helper won't recognize them once compressed
find %{buildroot}/lib/modules/%{kernel_file_string}/kernel -name *.ko \
    -exec objcopy --only-keep-debug '{}' '{}'.debug \;
find %{buildroot}/lib/modules/%{kernel_file_string}/kernel -name *.ko \
    -exec objcopy --add-gnu-debuglink='{}'.debug --strip-debug '{}' \;
find %{buildroot}/lib/modules/%{kernel_file_string}/kernel -name *.ko.debug | \
    sed -e 's|%{buildroot}||' > kernel_debug_files

# compress modules
find %{buildroot}/lib/modules/%{kernel_file_string} -name *.ko | xargs gzip -9
/sbin/depmod -u -ae -b %{buildroot} -r \
    -F %{buildroot}/boot/System.map-%{kernel_file_string} \
    %{kernel_file_string}

# create modules description
pushd %{buildroot}/lib/modules/%{kernel_file_string}
find . -name *.ko.gz | xargs /sbin/modinfo | \
    perl -lne 'print "$name\t$1" if $name && /^description:\s*(.*)/; $name = $1 if m!^filename:\s*(.*)\.k?o!; $name =~ s!.*/!!' \
    > modules.description
popd

# install kernel sources
install -d -m 755 %{buildroot}%{_prefix}/src/linux-%{kernel_file_string}
tar xjf %{SOURCE0} \
    -C %{buildroot}%{_prefix}/src/linux-%{kernel_file_string} \
    --strip-components=1

# clean sources from useless source files
pushd %{buildroot}%{_prefix}/src/linux-%{kernel_file_string}
for i in alpha arm arm26 avr32 blackfin cris frv h8300 ia64 m32r mips m68k \
         m68knommu mn10300 parisc powerpc s390 sh sh64 sparc sparc64 v850 xtensa
do
	rm -rf arch/$i
	rm -rf include/asm-$i
done
popd

%post -n kernel-xen-devel-%{kernel_package_string}
if [ -d /lib/modules/%{kernel_file_string} ]; then
    ln -sTf /usr/src/linux-%{kernel_file_string} /lib/modules/%{kernel_file_string}/build
    ln -sTf /usr/src/linux-%{kernel_file_string} /lib/modules/%{kernel_file_string}/source
fi

%postun -n kernel-xen-devel-%{kernel_package_string}
if [ -L /lib/modules/%{kernel_file_string}/build ]; then
    rm -f /lib/modules/%{kernel_file_string}/build
fi
if [ -L /lib/modules/%{kernel_file_string}/source ]; then
    rm -f /lib/modules/%{kernel_file_string}/source
fi

%clean
rm -rf %{buildroot}

%files -n kernel-xen-%{kernel_package_string}
%defattr(-,root,root)
/lib/modules/%{kernel_file_string}
/boot/System.map-%{kernel_file_string}
/boot/config-%{kernel_file_string}
/boot/vmlinuz-%{kernel_file_string}

%files -n kernel-xen-devel-%{kernel_package_string}
%defattr(-,root,root)
%{_prefix}/src/linux-%{kernel_file_string}

%files -n kernel-xen-debug-%{kernel_package_string} -f kernel_debug_files
%defattr(-,root,root)
