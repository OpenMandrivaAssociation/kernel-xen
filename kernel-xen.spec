%define name                    kernel-xen
%define version                 2.6.33
%define rel                     1
%define kernel_version          2.6.33
%define kernel_extraversion     xen-%{rel}mdv
# ensures file uniqueness
%define kernel_file_string      %{kernel_version}-xen-%{rel}mdv
# ensures package uniqueness
%define kernel_package_string   %{kernel_version}-%{rel}mdv
%define kernel_source_dir       %{_prefix}/src/kernel-xen-%{kernel_version}-%{rel}mdv
%define kernel_devel_dir        %{_prefix}/src/kernel-xen-devel-%{kernel_version}-%{rel}mdv

%define _default_patch_fuzz 2

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

Source12:   disable-mrproper-in-devel-rpms.patch
Source13:   kbuild-really-dont-remove-bounds-asm-offsets-headers.patch
Patch60000: 60000_add-console-use-vt.patch1
Patch60001: 60001_linux-2.6.19-rc1-kexec-move_segment_code-i386.patch1
Patch60002: 60002_linux-2.6.19-rc1-kexec-move_segment_code-x86_64.patch1
Patch60003: 60003_ipv6-no-autoconf.patch1
Patch60004: 60004_pci-guestdev.patch1
Patch60005: 60005_pci-reserve.patch1
Patch60006: 60006_xen3-auto-xen-arch.patch1
Patch60007: 60007_xen3-auto-xen-drivers.patch1
Patch60008: 60008_xen3-auto-include-xen-interface.patch1
Patch60009: 60009_xen3-auto-xen-kconfig.patch1
Patch60010: 60010_xen3-auto-common.patch1
Patch60011: 60011_xen3-auto-arch-x86.patch1
Patch60012: 60012_xen3-auto-arch-i386.patch1
Patch60013: 60013_xen3-auto-arch-x86_64.patch1
Patch60014: 60014_xen3-fixup-xen.patch1
Patch60015: 60015_xen3-fixup-kconfig.patch1
Patch60016: 60016_xen3-fixup-common.patch1
Patch60017: 60017_xen3-fixup-arch-x86.patch1
Patch60018: 60018_xen3-patch-2.6.18.patch1
Patch60019: 60019_xen3-patch-2.6.19.patch1
Patch60020: 60020_xen3-patch-2.6.20.patch1
Patch60021: 60021_xen3-patch-2.6.21.patch1
Patch60022: 60022_xen3-patch-2.6.22.patch1
Patch60023: 60023_xen3-patch-2.6.23.patch1
Patch60024: 60024_xen3-patch-2.6.24.patch1
Patch60025: 60025_xen3-patch-2.6.25.patch1
Patch60026: 60026_xen3-patch-2.6.26.patch1
Patch60027: 60027_xen3-patch-2.6.27.patch1
Patch60028: 60028_xen3-patch-2.6.28.patch1
Patch60029: 60029_xen3-patch-2.6.29.patch1
Patch60030: 60030_xen3-patch-2.6.30.patch1
Patch60031: 60031_xen3-patch-2.6.31.patch1
Patch60032: 60032_xen3-patch-2.6.32.patch1
Patch60033: 60033_xen3-patch-2.6.33.patch1
Patch60034: 60034_xen-balloon-max-target.patch1
Patch60035: 60035_xen-blkback-cdrom.patch1
Patch60036: 60036_xen-blktap-write-barriers.patch1
Patch60037: 60037_xen-op-packet.patch1
Patch60038: 60038_xen-blkfront-cdrom.patch1
Patch60039: 60039_xen-sections.patch1
Patch60040: 60040_xen-kconfig-compat.patch1
Patch60041: 60041_xen-cpufreq-report.patch1
Patch60042: 60042_xen-staging-build.patch1
Patch60043: 60043_xen-sysdev-suspend.patch1
Patch60044: 60044_xen-ipi-per-cpu-irq.patch1
Patch60045: 60045_xen-virq-per-cpu-irq.patch1
Patch60046: 60046_xen-clockevents.patch1
Patch60047: 60047_xen-spinlock-poll-early.patch1
Patch60048: 60048_xen-configurable-guest-devices.patch1
Patch60049: 60049_xen-netback-nr-irqs.patch1
Patch60050: 60050_xen-netback-notify-multi.patch1
Patch60051: 60051_xen-netback-generalize.patch1
Patch60052: 60052_xen-netback-multiple-tasklets.patch1
Patch60053: 60053_xen-netback-kernel-threads.patch1
Patch60054: 60054_xen-unpriv-build.patch1
Patch60055: 60055_xen-x86-panic-no-reboot.patch1
Patch60056: 60056_xen-x86-dcr-fallback.patch1
Patch60057: 60057_xen-x86-consistent-nmi.patch1
Patch60058: 60058_xen-x86-no-lapic.patch1
Patch60059: 60059_xen-x86-pmd-handling.patch1
Patch60060: 60060_xen-x86-bigmem.patch1
Patch60061: 60061_xen-x86-machphys-prediction.patch1
Patch60062: 60062_xen-x86-exit-mmap.patch1
Patch60063: 60063_xen-x86-per-cpu-vcpu-info.patch1
Patch60064: 60064_xen-x86_64-pgd-pin.patch1
Patch60065: 60065_xen-x86_64-pgd-alloc-order.patch1
Patch60066: 60066_xen-x86_64-dump-user-pgt.patch1
Patch60067: 60067_xen-x86_64-note-init-p2m.patch1
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
Requires(post):	bootloader-utils mkinitrd xen-hypervisor
Requires(postun):	bootloader-utils

%description -n kernel-xen-%{kernel_package_string}
The XEN kernel.

%package -n kernel-xen-devel-%{kernel_package_string}
Version:    1
Release:    %mkrel 1
Summary:    XEN kernel devel files
Group:      System/Kernel and hardware
Provides:   kernel-devel = %{kernel_version}
Autoreqprov: no

%description -n kernel-xen-devel-%{kernel_package_string}
This package contains the kernel-devel files that should be enough to build 
3rdparty drivers against for use with the %{kname}-%{buildrel}.

%package -n kernel-xen-source-%{kernel_package_string}
Version:    1
Release:    %mkrel 1
Summary:    XEN kernel sources
Group:      System/Kernel and hardware
Provides:   kernel-source = %{kernel_version}
Autoreqprov: no

%description -n kernel-xen-source-%{kernel_package_string}
This package contains the source code files for the Linux 
kernel. Theese source files are only needed if you want to build your own 
custom kernel that is better tuned to your particular hardware.

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

%package -n kernel-xen-doc-%{kernel_package_string}
Version:    1
Release:    %mkrel 1
Summary:    XEN kernel documentation
Group:      System/Kernel and hardware
Autoreqprov: no

%description -n kernel-xen-doc-%{kernel_package_string}
This package contains documentation files form the kernel source. Various
bits of information about the Linux kernel and the device drivers shipped
with it are documented in these files. You also might want install this
package if you need a reference to the options that can be passed to Linux
kernel modules at load time.

%prep
%setup -q -n linux-%{kernel_version}
%patch60000 -p 1
%patch60001 -p 1
%patch60002 -p 1
%patch60003 -p 1
%patch60004 -p 1
%patch60005 -p 1
%patch60006 -p 1
%patch60007 -p 1
%patch60008 -p 1
%patch60009 -p 1
%patch60010 -p 1
%patch60011 -p 1
%patch60012 -p 1
%patch60013 -p 1
%patch60014 -p 1
%patch60015 -p 1
%patch60016 -p 1
%patch60017 -p 1
%patch60018 -p 1
%patch60019 -p 1
%patch60020 -p 1
%patch60021 -p 1
%patch60022 -p 1
%patch60023 -p 1
%patch60024 -p 1
%patch60025 -p 1
%patch60026 -p 1
%patch60027 -p 1
%patch60028 -p 1
%patch60029 -p 1
%patch60030 -p 1
%patch60031 -p 1
%patch60032 -p 1
%patch60033 -p 1
%patch60034 -p 1
%patch60035 -p 1
%patch60036 -p 1
%patch60037 -p 1
%patch60038 -p 1
%patch60039 -p 1
%patch60040 -p 1
%patch60041 -p 1
%patch60042 -p 1
%patch60043 -p 1
%patch60044 -p 1
%patch60045 -p 1
%patch60046 -p 1
%patch60047 -p 1
%patch60048 -p 1
%patch60049 -p 1
%patch60050 -p 1
%patch60051 -p 1
%patch60052 -p 1
%patch60053 -p 1
%patch60054 -p 1
%patch60055 -p 1
%patch60056 -p 1
%patch60057 -p 1
%patch60058 -p 1
%patch60059 -p 1
%patch60060 -p 1
%patch60061 -p 1
%patch60062 -p 1
%patch60063 -p 1
%patch60064 -p 1
%patch60065 -p 1
%patch60066 -p 1
%patch60067 -p 1

%build
perl -p \
    -e 's/CONFIG_LOCALVERSION=.*/CONFIG_LOCALVERSION="-%{kernel_extraversion}"/' \
    < %config > .config
%make oldconfig
%make
%make modules

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/boot
install -m 644 System.map %{buildroot}/boot/System.map-%{kernel_file_string}
install -m 644 .config %{buildroot}/boot/config-%{kernel_file_string}
install -m 644 arch/x86/boot/vmlinuz \
    %{buildroot}/boot/vmlinuz-%{kernel_file_string}

# modules
%make modules_install INSTALL_MOD_PATH=%{buildroot}

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
    sed -e 's|%{buildroot}||' > kernel_debug_files.list

# create an exclusion list for those debug files
sed -e 's|^|%exclude |' < kernel_debug_files.list > no_kernel_debug_files.list

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
install -d -m 755 %{buildroot}%{kernel_source_dir}
tar cf - . \
    --exclude '*.o' --exclude '*.ko'  --exclude '*.cmd' \
    --exclude '.temp*' --exclude '.tmp*' \
    --exclude modules.order --exclude .gitignore \
    | tar xf - -C %{buildroot}%{kernel_source_dir}
chmod -R a+rX %{buildroot}%{kernel_source_dir}

# we remove all the source files that we don't ship
# first architecture files
for i in alpha arm arm26 avr32 blackfin cris frv h8300 ia64 microblaze mips \
    m32r m68k m68knommu mn10300 parisc powerpc ppc s390 sh sh64 sparc v850 xtensa; do
    rm -rf %{buildroot}%{kernel_source_dir}/arch/$i
    rm -rf %{buildroot}%{kernel_source_dir}/include/asm-$i
done

%ifnarch %{ix86} x86_64
    rm -rf %{buildroot}%{kernel_source_dir}/arch/x86
    rm -rf %{buildroot}%{kernel_source_dir}/include/asm-x86
%endif

rm -rf %{buildroot}%{kernel_source_dir}/vmlinux
rm -rf %{buildroot}%{kernel_source_dir}/System.map
rm -rf %{buildroot}%{kernel_source_dir}/Module.*
rm -rf %{buildroot}%{kernel_source_dir}/*.list
rm -rf %{buildroot}%{kernel_source_dir}/.config.*
rm -rf %{buildroot}%{kernel_source_dir}/.missing-syscalls.d
rm -rf %{buildroot}%{kernel_source_dir}/.version
rm -rf %{buildroot}%{kernel_source_dir}/.mailmap

# install devel files 
install -d -m 755 %{buildroot}%{kernel_devel_dir}
for i in $(find . -name 'Makefile*'); do
    cp -R --parents $i %{buildroot}%{kernel_devel_dir};
done
for i in $(find . -name 'Kconfig*' -o -name 'Kbuild*'); do
    cp -R --parents $i %{buildroot}%{kernel_devel_dir};
done
cp -fR include %{buildroot}%{kernel_devel_dir}
cp -fR scripts %{buildroot}%{kernel_devel_dir}
%ifarch %{ix86} x86_64
    cp -fR arch/x86/kernel/asm-offsets.{c,s} \
        %{buildroot}%{kernel_devel_dir}/arch/x86/kernel/
    cp -fR arch/x86/kernel/asm-offsets_{32,64}.c \
        %{buildroot}%{kernel_devel_dir}/arch/x86/kernel/
    cp -fR arch/x86/include %{buildroot}%{kernel_devel_dir}/arch/x86/
%else
    cp -fR arch/%{target_arch}/kernel/asm-offsets.{c,s} \
        %{buildroot}%{kernel_devel_dir}/arch/%{target_arch}/kernel/
    cp -fR arch/%{target_arch}/include \
        %{buildroot}%{kernel_devel_dir}/arch/%{target_arch}/
%endif
cp -fR .config Module.symvers %{buildroot}%{kernel_devel_dir}

# Needed for truecrypt build (Danny)
cp -fR drivers/md/dm.h %{buildroot}%{kernel_devel_dir}/drivers/md/

# Needed for external dvb tree (#41418)
cp -fR drivers/media/dvb/dvb-core/*.h \
    %{buildroot}%{kernel_devel_dir}/drivers/media/dvb/dvb-core/
cp -fR drivers/media/dvb/frontends/lgdt330x.h \
    %{buildroot}%{kernel_devel_dir}/drivers/media/dvb/frontends/

# add acpica header files, needed for fglrx build
cp -fR drivers/acpi/acpica/*.h \
    %{buildroot}%{kernel_devel_dir}/drivers/acpi/acpica/

# disable mrproper
patch -p1 -d %{buildroot}%{kernel_devel_dir} -i %{SOURCE12}

# disable bounds.h and asm-offsets.h removal
patch -p1 -d %{buildroot}%{kernel_devel_dir} -i %{SOURCE13}

%post -n kernel-xen-%{kernel_package_string}
/sbin/installkernel %{kernel_file_string}
pushd /boot > /dev/null
if [ -L vmlinuz-xen ]; then
        rm -f vmlinuz-xen
fi
ln -sf vmlinuz-%{kernel_file_string} vmlinuz-xen
if [ -L initrd-xen.img ]; then
        rm -f initrd-xen.img
fi
ln -sf initrd-%{kernel_file_string}.img initrd-xen.img
popd > /dev/null

%postun -n kernel-xen-%{kernel_package_string}
/sbin/installkernel -R %{kernel_file_string}
pushd /boot > /dev/null
if [ -L vmlinuz-xen ]; then
        if [ "$(readlink vmlinuz-xen)" = "vmlinuz-%{kernel_file_string}" ]; then
                rm -f vmlinuz-xen
        fi
fi
if [ -L initrd-xen.img ]; then
        if [ "$(readlink initrd-xen.img)" = "initrd-%{kernel_file_string}.img" ]; then
                rm -f initrd-xen.img
        fi
fi
popd > /dev/null

%post -n kernel-xen-devel-%{kernel_package_string}
if [ -d /lib/modules/%{kernel_file_string} ]; then
    ln -sf %{kernel_devel_dir} /lib/modules/%{kernel_file_string}/build
    ln -sf %{kernel_devel_dir} /lib/modules/%{kernel_file_string}/source
fi

%preun -n kernel-xen-devel-%{kernel_package_string}
if [ -L /lib/modules/%{kernel_file_string}/build ]; then
    rm -f /lib/modules/%{kernel_devel_string}/build
fi
if [ -L /lib/modules/%{kernel_file_string}/source ]; then
    rm -f /lib/modules/%{kernel_devel_string}/source
fi

%post -n kernel-xen-source-%{kernel_package_string}
if [ -d /lib/modules/%{kernel_file_string} ]; then
    ln -sf %{kernel_source_dir} /lib/modules/%{kernel_file_string}/build
    ln -sf %{kernel_source_dir} /lib/modules/%{kernel_file_string}/source
fi

%preun -n kernel-xen-source-%{kernel_package_string}
if [ -L /lib/modules/%{kernel_file_string}/build ]; then
    rm -f /lib/modules/%{kernel_source_string}/build
fi
if [ -L /lib/modules/%{kernel_file_string}/source ]; then
    rm -f /lib/modules/%{kernel_source_string}/source
fi

%clean
rm -rf %{buildroot}

%files -n kernel-xen-%{kernel_package_string} -f no_kernel_debug_files.list
%defattr(-,root,root)
/lib/modules/%{kernel_file_string}
/boot/System.map-%{kernel_file_string}
/boot/config-%{kernel_file_string}
/boot/vmlinuz-%{kernel_file_string}

%files -n kernel-xen-devel-%{kernel_package_string}
%defattr(-,root,root)
%{kernel_devel_dir}

%files -n kernel-xen-source-%{kernel_package_string}
%defattr(-,root,root)
%{kernel_source_dir}
%exclude %{kernel_source_dir}/Documentation

%files -n kernel-xen-doc-%{kernel_package_string}
%defattr(-,root,root)
%{kernel_source_dir}/Documentation

%files -n kernel-xen-debug-%{kernel_package_string} -f kernel_debug_files.list
%defattr(-,root,root)
