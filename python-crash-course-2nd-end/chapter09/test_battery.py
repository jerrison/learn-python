import unittest
import io
from contextlib import redirect_stdout
from battery import Battery

class TestBattery(unittest.TestCase):
    """Tests for the class Battery."""

    def test_get_range_75(self):
        """Test get_range for battery size 75."""
        battery = Battery(75)
        f = io.StringIO()
        with redirect_stdout(f):
            battery.get_range()
        output = f.getvalue().strip()
        self.assertEqual(output, "This car can go about 260 miles on a full charge.")

    def test_get_range_100(self):
        """Test get_range for battery size 100."""
        battery = Battery(100)
        f = io.StringIO()
        with redirect_stdout(f):
            battery.get_range()
        output = f.getvalue().strip()
        self.assertEqual(output, "This car can go about 315 miles on a full charge.")

    def test_get_range_other_size(self):
        """Test get_range for a battery size other than 75 or 100."""
        battery = Battery(85)
        f = io.StringIO()
        with redirect_stdout(f):
            battery.get_range()
        output = f.getvalue().strip()
        # 85 * 3.5 = 297.5
        self.assertEqual(output, "This car can go about 297.5 miles on a full charge.")

if __name__ == '__main__':
    unittest.main()
