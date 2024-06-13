import logging

import numpy as np
import pandas as pd
import pytest

import physiofit
import physiofit.base.io

logging.getLogger("physiofit").setLevel(logging.ERROR)


@pytest.fixture
def model_2_data():

    return pd.DataFrame(
        {'time': {0: 0.0, 1: 0.2, 2: 0.4, 3: 0.6000000000000001, 4: 0.8,
                  5: 1.0, 6: 1.2000000000000002, 7: 1.4000000000000001, 8: 1.6,
                  9: 1.8, 10: 2.0, 11: 2.2, 12: 2.4000000000000004, 13: 2.6,
                  14: 2.8000000000000003, 15: 3.0, 16: 3.2,
                  17: 3.4000000000000004, 18: 3.6, 19: 3.8000000000000003,
                  20: 4.0, 21: 4.2, 22: 4.4, 23: 4.6000000000000005,
                  24: 4.800000000000001, 25: 5.0, 26: 5.2, 27: 5.4,
                  28: 5.6000000000000005, 29: 5.800000000000001},
         'X': {0: 0.02, 1: 0.02, 2: 0.02, 3: 0.02, 4: 0.02, 5: 0.02, 6: 0.02,
               7: 0.020000000000000004, 8: 0.02347021741983621,
               9: 0.027542555286719145, 10: 0.03232148804385787,
               11: 0.037929617586099036, 12: 0.04451081856984937,
               13: 0.052233929468462365, 14: 0.061297084065860055,
               15: 0.07193279451138565, 16: 0.08441391633993109,
               17: 0.09906064848790236, 18: 0.1162487478880518,
               19: 0.13641916938581505, 20: 0.16008937828592706,
               21: 0.18786662574885568, 22: 0.2204635276128321,
               23: 0.25871634631086166, 24: 0.3036064448990781,
               25: 0.3562854635922441, 26: 0.4181048647018553,
               27: 0.49065060394218707, 28: 0.5757838175848543,
               29: 0.6756885692769915},
         'Glucose': {0: 20.0, 1: 20.0, 2: 20.0, 3: 20.0, 4: 20.0, 5: 20.0,
                     6: 20.0, 7: 20.0, 8: 19.96529782580164,
                     9: 19.92457444713281, 10: 19.876785119561422,
                     11: 19.82070382413901, 12: 19.754891814301505,
                     13: 19.677660705315375, 14: 19.587029159341398,
                     15: 19.480672054886142, 16: 19.35586083660069,
                     17: 19.209393515120976, 18: 19.03751252111948,
                     19: 18.83580830614185, 20: 18.59910621714073,
                     21: 18.32133374251144, 22: 17.99536472387168,
                     23: 17.612836536891383, 24: 17.163935551009217,
                     25: 16.63714536407756, 26: 16.018951352981446,
                     27: 15.293493960578129, 28: 14.442161824151459,
                     29: 13.443114307230086},
         'Acetate': {0: 0.01, 1: 0.01, 2: 0.01, 3: 0.01, 4: 0.01, 5: 0.01,
                     6: 0.01, 7: 0.010000000000000018, 8: 0.02301331532438579,
                     9: 0.03828458232519679, 10: 0.05620558016446701,
                     11: 0.07723606594787139, 12: 0.10191556963693511,
                     13: 0.13087723550673386, 14: 0.16486406524697522,
                     15: 0.2047479794176962, 16: 0.2515521862747415,
                     17: 0.30647743182963383, 18: 0.37093280458019423,
                     19: 0.4465718851968064, 20: 0.5353351685722265,
                     21: 0.6394998465582088, 22: 0.7617382285481203,
                     23: 0.9051862986657312, 24: 1.0735241683715429,
                     25: 1.2710704884709152, 26: 1.5028932426319574,
                     27: 1.7749397647832015, 28: 2.0941893159432032,
                     29: 2.4688321347887174},
         'Glutamate': {0: 0.01, 1: 0.01, 2: 0.01, 3: 0.01, 4: 0.01, 5: 0.01,
                       6: 0.01, 7: 0.01000000000000001,
                       8: 0.018675543549590525, 9: 0.02885638821679786,
                       10: 0.04080372010964467, 11: 0.05482404396524759,
                       12: 0.0712770464246234, 13: 0.0905848236711559,
                       14: 0.11324271016465012, 15: 0.13983198627846413,
                       16: 0.1710347908498277, 17: 0.20765162121975586,
                       18: 0.25062186972012945, 19: 0.30104792346453757,
                       20: 0.3602234457148176, 21: 0.4296665643721392,
                       22: 0.5111588190320802, 23: 0.6067908657771541,
                       24: 0.7190161122476952, 25: 0.8507136589806101,
                       26: 1.0052621617546382, 27: 1.1866265098554676,
                       28: 1.3994595439621356, 29: 1.6492214231924784}}
    )


def test_model_2_estimation(
        model_2_data: pd.DataFrame,
        sds: physiofit.models.base_model.StandardDevs
):
    io = physiofit.base.io.IoHandler()
    model = io.select_model(
        name="Steady-state batch model with lag phase",
        data=model_2_data
    )
    model.get_params()
    fitter = io.initialize_fitter(
        data=model.data,
        model=model,
        sd=sds,
        debug_mode=False
    )
    fitter.optimize()

    assert np.allclose(
        a=fitter.parameter_stats["optimal"],
        b=[0.02, 0.8, 1.4, -8, 20, 3, 0.01, 2, 0.01],
        rtol=1e-3
    )


def test_model_2_simulation(
        placeholder_data,
        parameters,
        model_2_data
):
    io = physiofit.base.io.IoHandler()
    model = io.select_model(
        name="Steady-state batch model with lag phase",
        data=placeholder_data
    )
    model.get_params()
    model.parameters.update(parameters)
    sim_data = model.simulate(
        list(model.parameters.values()),
        model.data.drop("time", axis=1),
        model.time_vector,
        model.args
    )
    df = pd.DataFrame(
        data=sim_data,
        index=model.time_vector,
        columns=model.name_vector
    )
    df.index.name = "time"

    pd.testing.assert_frame_equal(
        df.reset_index(),
        model_2_data,
        atol=1e-6
    )
