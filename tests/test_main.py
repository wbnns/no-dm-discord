import unittest
from unittest.mock import patch
from no_dm_discord.main import update_discord_status

class TestUpdateDiscordStatus(unittest.TestCase):
    @patch('no_dm_discord.main.requests.put')
    def test_update_discord_status_success(self, mock_put):
        # Setup the mock to simulate a successful API response
        mock_put.return_value.status_code = 200

        # Execute the function under test
        update_discord_status()

        # Assertions to ensure the function behaved as expected
        self.assertTrue(mock_put.called, "The requests.put method was not called.")

if __name__ == '__main__':
    unittest.main()

