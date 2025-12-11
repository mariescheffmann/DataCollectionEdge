import unittest
from unittest.mock import patch

with patch('MqttPublisher.MqttPublisher'):
    from Data import RealTimeData, AnalyticsData

class TestRealTimeData(unittest.TestCase):

    test_data = {
        "name": "test",
        "value": 2,
        "timestamp": '2025-11-27T15:10:32.545461',
        "tag": "testTag"
    }

    def setUp(self):
        self.real_time_data = RealTimeData(
            'test',
            2,
            'testRealTimeDatabase',
            '2025-11-27T15:10:32.545461',
            'testTag'
        )

    def test_prepare_data(self):
        self.assertEqual(
            self.real_time_data.toRealtimeJson(),
            self.test_data,
            'Data was not prepared correctly.'
        )


class TestAnalyticsData(unittest.TestCase):

    test_sql_data = {
        "machine_id": 1,
        "event_name": "TestEvent",
        "opcua_value": "test:opcua:value",
        "template_config": {"key": "value"},
        "timestamp": "2025-11-27T15:10:32.545461"
    }

    def setUp(self):
        self.sql_data = AnalyticsData(
            1,
            "TestEvent",
            "test:opcua:value",
            {"key": "value"},
            "2025-11-27T15:10:32.545461"
        )

    def test_toSQLJson(self):
        self.assertEqual(
            self.sql_data.toSQLJson(),
            self.test_sql_data,
            'SQL Data was not prepared correctly'
        )


if __name__ == '__main__':
    unittest.main()