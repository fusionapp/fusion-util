from incremental import Version
from twisted.trial.unittest import SynchronousTestCase

from fusion_util.cert import chainCerts



class chainCertTests(SynchronousTestCase):
    """
    Tests for L{chainCerts}.
    """
    def test_chainCerts(self):
        """
        ``chainCerts`` emits a deprecation warning.
        """
        self.assertEqual(
            [],
            self.callDeprecated(
                (Version('fusion_util', 'NEXT', 0, 0), 'pem.twisted'),
                chainCerts, ''))
