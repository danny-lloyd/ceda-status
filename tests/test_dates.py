import unittest

from pydantic import ValidationError

from testing_ceda_status.model import StatusPage


class CheckDates(unittest.TestCase):

    def test_model(self) -> None:

        bad_json = """
                [
                    {
                        "status": "degraded",
                        "affectedServices": "SOF storage",
                        "summary": "Issue affecting SOF storage used for /gws/nopw/j04/* workspaces & CEDA archive.",
                        "date": "2024-06-14Ta08:15",
                        "updates": [
                            {
                                "date": "2024-06-24T09:25",
                                "details": "Registry issue now resolved after some host reboots. Quota issue persists, see previous update."
                            }
                        ]
                    }
                ]
            """

        with self.assertRaises(ValidationError):
            StatusPage.model_validate_json(bad_json)


if __name__ == "__main__":
    unittest.main()
