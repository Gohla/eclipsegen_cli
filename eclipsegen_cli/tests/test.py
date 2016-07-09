from unittest import TestCase

from eclipsegen_cli.main import main


class Test(TestCase):
  def test_main_help(self):
    ret = main('eclipsegen', '--help-all', exitAfter=False)
    self.assertEqual(ret, 0, 'Nonzero return code')

  def test_main_list_presets(self):
    ret = main('eclipsegen', 'list-presets', exitAfter=False)
    self.assertEqual(ret, 0, 'Nonzero return code')
