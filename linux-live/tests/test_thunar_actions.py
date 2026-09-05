#!/usr/bin/python3
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
XFCE = ROOT / 'linux-live/scripts/04-xfce-desktop'
ROOTCOPY = XFCE / 'rootcopy-install'
PACKAGE = ROOT / 'submodules/minios-thunar-integration'


class ThunarIntegrationBoundaryTests(unittest.TestCase):
    def test_thunar_binary_is_not_wrapped(self):
        install = (XFCE / 'install').read_text()
        self.assertNotIn('thunar-bin', install)
        self.assertFalse((ROOTCOPY / 'usr/bin/thunar.sh').exists())
        self.assertFalse((ROOTCOPY / 'usr/bin/thunar').exists())

    def test_xfce_module_consumes_packaged_integration(self):
        packages = (XFCE / 'packages.list').read_text().splitlines()
        self.assertIn('minios-thunar-integration', packages)
        for relative in (
                'usr/bin/minios-thunar-actions',
                'usr/bin/minios-thunar-uca-sync',
                'etc/X11/Xsession.d/65minios-thunar-uca-sync',
                'etc/xdg/autostart/minios-thunar-uca-sync.desktop'):
            self.assertFalse((ROOTCOPY / relative).exists(), relative)

    def test_old_uca_copies_are_gone(self):
        thunar_dir = ROOTCOPY / 'etc/skel/.config/Thunar'
        if thunar_dir.exists():
            self.assertEqual(list(thunar_dir.glob('uca*.xml')), [])

    def test_direct_xfce_start_paths_sync_before_session(self):
        for startup in (ROOTCOPY / 'etc/skel/.xinitrc', ROOTCOPY / 'etc/skel/.xsession'):
            text = startup.read_text()
            self.assertIn('/usr/bin/minios-thunar-uca-sync', text)
            self.assertLess(text.index('minios-thunar-uca-sync'), text.index('xfce4-session'))

    def test_package_owns_the_thunar_frontend(self):
        self.assertTrue((PACKAGE / 'bin/minios-thunar-actions').is_file())
        self.assertTrue((PACKAGE / 'bin/minios-thunar-uca-sync').is_file())
        self.assertFalse(any(ROOTCOPY.rglob('minios-thunar-actions.mo')))


if __name__ == '__main__':
    unittest.main()
