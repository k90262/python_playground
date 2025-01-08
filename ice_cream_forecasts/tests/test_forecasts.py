import datetime

import approvaltests

from forecasts import print_sales_forecasts_with_update_selection
from scorer import IceCream
import scorer


def test_sales_forecasts(capsys):
    print_sales_forecasts_with_update_selection(
        now=datetime.datetime.fromisoformat("2025-01-08 18:08:53.024945"),
        update_selection=stub_update_selection
    )
    output = capsys.readouterr()
    approvaltests.verify(output.out)

def stub_update_selection():
    scorer.flavour = IceCream.Vanilla