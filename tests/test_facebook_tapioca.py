# coding: utf-8

import unittest

from tapioca_facebook import Facebook


class TestTapioca(unittest.TestCase):

    def setUp(self):
        self.wrapper = Facebook(client_id='client_id', access_token='access_token')

    def test_resource_access(self):
        resource = self.wrapper.user_feed(id='me')

        self.assertEqual(resource.data(), 'https://graph.facebook.com/me/feed')



if __name__ == '__main__':
    unittest.main()
