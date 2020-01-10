%define name                    kernel-xen
%define version                 2.6.32.11
%define rel                     3
%define kernel_version          2.6.32.11
%define kernel_extraversion     xen-%{rel}mdv
# ensures file uniqueness
%define kernel_file_string      %{kernel_version}-%{kernel_extraversion}
# ensures package uniqueness
%define kernel_package_string   %{kernel_version}-%{rel}mdv
%define kernel_source_dir       %{_prefix}/src/%{name}-%{kernel_package_string}
%define kernel_devel_dir        %{_prefix}/src/%{name}-devel-%{kernel_package_string}

%define _default_patch_fuzz 3

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
Source0:    linux-%{kernel_version}.tar.bz2
Source1:    i386_defconfig-server
Source2:    x86_64_defconfig-server

Source12:   disable-mrproper-in-devel-rpms.patch
Source13:   kbuild-really-dont-remove-bounds-asm-offsets-headers.patch
# suze patches
Patch90:    bug-561933_uv_pat_is_gru_range.patch
Patch91:    x86-Unify-fixup_irqs-for-32-bit-and-64-bit-kernels.patch
Patch92:    SoN-23-mm-swapfile.patch
Patch93:    x86-cpu-mv-display_cacheinfo-cpu_detect_cache_sizes.patch
Patch94:    fix_clock_gettime_vsyscall_time_warp.diff
### both uml framebuffer and xen need this one.
Patch100:   add-console-use-vt
# split out patches
Patch101:   linux-2.6.19-rc1-kexec-move_segment_code-i386.patch
Patch102:   linux-2.6.19-rc1-kexec-move_segment_code-x86_64.patch
Patch103:   ipv6-no-autoconf
Patch104:   pci-guestdev
Patch105:   pci-reserve
Patch106:   sfc-driverlink
Patch107:   sfc-resource-driver
Patch108:   sfc-driverlink-conditional
Patch109:   sfc-external-sram
Patch110:   tmem
# bulk stuff, new files for xen
Patch200:   xen3-auto-xen-arch.diff
Patch201:   xen3-auto-xen-drivers.diff
Patch202:   xen3-auto-include-xen-interface.diff
# kconfig bits for xen
Patch300:   xen3-auto-xen-kconfig.diff
# common code changes
Patch400:   xen3-auto-common.diff
Patch401:   xen3-auto-arch-x86.diff
Patch402:   xen3-auto-arch-i386.diff
Patch403:   xen3-auto-arch-x86_64.diff
# fixups due to upstream Xen parts
Patch500:   xen3-fixup-xen
Patch501:   sfc-set-arch
Patch502:   sfc-endianness
# newer changeset backports
# changes outside arch/{i386,x86_64}/xen
Patch700:   xen3-fixup-kconfig
Patch701:   xen3-fixup-common
Patch702:   xen3-fixup-arch-x86
# ports of other patches
Patch800:   xen3-patch-2.6.18
Patch801:   xen3-patch-2.6.19
Patch802:   xen3-patch-2.6.20
Patch803:   xen3-patch-2.6.21
Patch804:   xen3-patch-2.6.22
Patch805:   xen3-patch-2.6.23
Patch806:   xen3-patch-2.6.24
Patch807:   xen3-patch-2.6.25
Patch808:   xen3-patch-2.6.26
Patch809:   xen3-patch-2.6.27
Patch810:   xen3-patch-2.6.28
Patch811:   xen3-patch-2.6.29
Patch812:   xen3-patch-2.6.30
Patch813:   xen3-patch-2.6.31
Patch814:   xen3-patch-2.6.32
Patch815:   xen3-patch-2.6.32.1-2
Patch816:   xen3-patch-2.6.32.2-3
Patch817:   xen3-patch-2.6.32.3-4
Patch818:   xen3-patch-2.6.32.7-8
Patch819:   xen3-patch-2.6.32.8-9
Patch820:   xen3-patch-2.6.32.9-10
Patch821:   xen3-seccomp-disable-tsc-option
Patch822:   xen3-fix_clock_gettime_vsyscall_time_warp.diff
Patch823:   xen3-x86-mcp51-no-dac
#Patch824:   xen3-x86-64-preserve-large-page-mapping-for-1st-2mb-kernel-txt-with-config_debug_rodata
#Patch825:   xen3-x86-64-align-rodata-kernel-section-to-2mb-with-config_debug_rodata
#Patch826:   xen3-x86-mark_rodata_rw.patch
#Patch827:   xen3-x86-ftrace-fix-rodata-1.patch
#Patch828:   xen3-x86-ftrace-fix-rodata-3.patch
Patch829:   xen3-x86-Remove-CPU-cache-size-output-for-non-Intel-too.patch
Patch830:   xen3-x86-cpu-mv-display_cacheinfo-cpu_detect_cache_sizes.patch
Patch831:   xen3-x86-Limit-the-number-of-processor-bootup-messages.patch
Patch832:   xen3-x86_64_apic_consider_hotplug_for_mode_logical_flat.patch
Patch833:   xen3-x86_ioapic_fix_out_of_order_gsi.patch
Patch834:   xen3-x86-Reduce-per-cpu-warning-boot-up-messages.patch
Patch835:   xen3-x86-pat-Update-page-flags-for-memtype-without-using-memtype_lock-V4.patch
Patch836:   xen3-bug-561933_uv_pat_is_gru_range.patch
Patch837:   xen3-x86-Fix-sched_clock_cpu-for-systems-with-unsynchronized-TSC.patch
Patch838:   xen3-x86-Unify-fixup_irqs-for-32-bit-and-64-bit-kernels.patch
Patch839:   xen3-x86-intr-remap-Avoid-irq_chip-mask-unmask-in-fixup_irqs-for-intr-remapping.patch
Patch840:   xen3-x86-Remove-local_irq_enable-local_irq_disable-in-fixup_irqs.patch
#Patch841:   xen3-vmw_pvscsi-scsi-driver-for-vmware-s-virtual-hba.patch
#Patch842:   xen3-add-support-for-intel-cougar-point-chipset.patch
#Patch843:   xen3-kdb-x86
Patch844:   xen3-stack-unwind
Patch845:   xen3-x86_64-unwind-annotations
# bugfixes and enhancements
Patch900:   xen-balloon-max-target
Patch901:   xen-modular-blktap
Patch902:   xen-blkback-bimodal-suse
Patch903:   xen-blkif-protocol-fallback-hack
Patch904:   xen-blkback-cdrom
Patch905:   xen-blktap-write-barriers
Patch906:   xen-op-packet
Patch907:   xen-blkfront-cdrom
Patch908:   xen-sections
Patch909:   xen-swiotlb-heuristics
Patch910:   xen-kconfig-compat
Patch911:   xen-cpufreq-report
Patch912:   xen-staging-build
Patch913:   xen-sysdev-suspend
Patch914:   xen-ipi-per-cpu-irq
Patch915:   xen-virq-per-cpu-irq
Patch916:   xen-spinlock-poll-early
Patch917:   xen-configurable-guest-devices
Patch918:   xen-netback-nr-irqs
Patch919:   xen-netback-notify-multi
Patch920:   xen-netback-generalize
Patch921:   xen-netback-multiple-tasklets
Patch922:   xen-netback-kernel-threads
Patch923:   xen-netfront-ethtool
Patch924:   xen-unpriv-build
Patch925:   xen-dcdbas
Patch926:   xen-floppy
Patch927:   xen-x86-panic-no-reboot
Patch928:   xen-x86-dcr-fallback
Patch929:   xen-x86-consistent-nmi
Patch930:   xen-x86-no-lapic
Patch931:   xen-x86-pmd-handling
Patch932:   xen-x86-bigmem
Patch933:   xen-x86-machphys-prediction
Patch934:   xen-x86-exit-mmap
Patch935:   xen-x86-per-cpu-vcpu-info
Patch936:   xen-x86-xtime-lock
Patch937:   xen-x86-time-per-cpu
Patch938:   xen-x86_64-pgd-pin
Patch939:   xen-x86_64-pgd-alloc-order
Patch940:   xen-x86_64-dump-user-pgt
Patch941:   xen-x86_64-note-init-p2m
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description 
The XEN kernel.

%package -n kernel-xen-%{kernel_package_string}
Version:    1
Release:    %mkrel 2
Summary:    XEN kernel
Group:      System/Kernel and hardware
Provides:   kernel = %{kernel_version}
Provides:   kernel-xen = %{kernel_version}
Requires(post):	bootloader-utils mkinitrd xen-hypervisor
Requires(postun):	bootloader-utils

%description -n kernel-xen-%{kernel_package_string}
The XEN kernel.

%package devel-%{kernel_package_string}
Version:    1
Release:    %mkrel 2
Summary:    XEN kernel devel files
Group:      System/Kernel and hardware
Provides:   kernel-devel = %{kernel_version}
Autoreqprov: no

%description devel-%{kernel_package_string}
This package contains the kernel-devel files that should be enough to build 
3rdparty drivers against for use with the %{kname}-%{buildrel}.

%package source-%{kernel_package_string}
Version:    1
Release:    %mkrel 2
Summary:    XEN kernel sources
Group:      System/Kernel and hardware
Provides:   kernel-source = %{kernel_version}
Autoreqprov: no

%description source-%{kernel_package_string}
This package contains the source code files for the Linux 
kernel. Theese source files are only needed if you want to build your own 
custom kernel that is better tuned to your particular hardware.

%package debug-%{kernel_package_string}
Version:  1
Release:  %mkrel 2
Summary:  Xen kernel debug files
Group:    Development/Debug
Requires: glibc-devel
Provides: kernel-debug = %{kernel_version}
Autoreqprov: no

%description debug-%{kernel_package_string}
This package contains the kernel-debug files that should be enough to 
use debugging/monitoring tool (like systemtap, oprofile, ...)

%package doc-%{kernel_package_string}
Version:    1
Release:    %mkrel 2
Summary:    XEN kernel documentation
Group:      System/Kernel and hardware
Autoreqprov: no

%description doc-%{kernel_package_string}
This package contains documentation files form the kernel source. Various
bits of information about the Linux kernel and the device drivers shipped
with it are documented in these files. You also might want install this
package if you need a reference to the options that can be passed to Linux
kernel modules at load time.

%prep
%setup -q -n linux-%{kernel_version}
%autopatch -p1

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
    --exclude '.temp*' --exclude '.tmp*' --exclude '*.0[0-9][0-9][0-9]' \
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

%post %{kernel_package_string}
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

%postun %{kernel_package_string}
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

%post devel-%{kernel_package_string}
if [ -d /lib/modules/%{kernel_file_string} ]; then
    ln -sf %{kernel_devel_dir} /lib/modules/%{kernel_file_string}/build
    ln -sf %{kernel_devel_dir} /lib/modules/%{kernel_file_string}/source
fi

%preun devel-%{kernel_package_string}
if [ -L /lib/modules/%{kernel_file_string}/build ]; then
    rm -f /lib/modules/%{kernel_devel_string}/build
fi
if [ -L /lib/modules/%{kernel_file_string}/source ]; then
    rm -f /lib/modules/%{kernel_devel_string}/source
fi

%post source-%{kernel_package_string}
if [ -d /lib/modules/%{kernel_file_string} ]; then
    ln -sf %{kernel_source_dir} /lib/modules/%{kernel_file_string}/build
    ln -sf %{kernel_source_dir} /lib/modules/%{kernel_file_string}/source
fi

%preun source-%{kernel_package_string}
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
