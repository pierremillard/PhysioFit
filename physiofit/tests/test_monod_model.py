"""
This module contains tests for the models module.
"""
import logging

import numpy as np
import pandas as pd
import pytest
from numpy import array

import physiofit

logging.getLogger("physiofit").setLevel(logging.ERROR)


@pytest.fixture
def pyfoomb_simulated_data():
    """
    Test data to use in tests for the Monod model. Data was simulated using
    the pyFOOMB package (see the `example 6 notebook <https://github.com/
    MicroPhen/pyFOOMB/blob/main/examples/Example06_BioprocessModels.ipynb>`_).
    """
    return pd.DataFrame.from_dict(
        {'time': array(
            [0.00000000e+00, 1.60350555e-06, 1.29272201e-02, 4.73210593e-02,
             8.17148984e-02, 1.16108738e-01, 1.68220493e-01, 2.20332247e-01,
             3.10246576e-01, 4.00160904e-01, 4.90075232e-01, 6.34757887e-01,
             7.79440543e-01, 9.24123199e-01, 1.21353541e+00, 1.50294763e+00,
             1.79235984e+00, 2.08177205e+00, 2.37118427e+00, 2.66059648e+00,
             2.95000869e+00, 3.23942091e+00, 3.52883312e+00, 3.81824533e+00,
             4.10765755e+00, 4.39706976e+00, 4.68648197e+00, 4.97589419e+00,
             5.26530640e+00, 5.55471861e+00, 5.75429441e+00, 5.95387020e+00,
             6.15344600e+00, 6.46543931e+00, 6.69021058e+00, 6.91498185e+00,
             7.13975312e+00, 7.36452439e+00, 7.58929566e+00, 7.81406694e+00,
             8.03883821e+00, 8.26360948e+00, 8.48838075e+00, 8.71315202e+00,
             8.93792329e+00, 9.29231855e+00, 9.64671381e+00, 9.87042767e+00,
             1.00941415e+01, 1.03178554e+01, 1.04707829e+01, 1.06237105e+01,
             1.07766381e+01, 1.08876690e+01, 1.09986998e+01, 1.11097307e+01,
             1.11913085e+01, 1.12728862e+01, 1.13544640e+01, 1.14360417e+01,
             1.14912119e+01, 1.15463820e+01, 1.16015522e+01, 1.16567224e+01,
             1.17118925e+01, 1.17670627e+01, 1.18060238e+01, 1.18344243e+01,
             1.18628249e+01, 1.18912255e+01, 1.19196261e+01, 1.19480267e+01,
             1.19764272e+01, 1.20048278e+01, 1.20247743e+01, 1.20447208e+01,
             1.20646672e+01, 1.20846137e+01, 1.21045602e+01, 1.21245066e+01,
             1.21444531e+01, 1.21685210e+01, 1.21859235e+01, 1.22033260e+01,
             1.22207286e+01, 1.22381311e+01, 1.22555336e+01, 1.22729361e+01,
             1.22903386e+01, 1.23166077e+01, 1.23428768e+01, 1.23691459e+01,
             1.23954150e+01, 1.24216840e+01, 1.24479531e+01, 1.24742222e+01,
             1.25004913e+01, 1.25267604e+01, 1.25530294e+01, 1.25792985e+01,
             1.26055676e+01, 1.26318367e+01, 1.26581058e+01, 1.26843748e+01,
             1.27106439e+01, 1.27369130e+01, 1.27631821e+01, 1.27894512e+01,
             1.28157202e+01, 1.28419893e+01, 1.28682584e+01, 1.28945275e+01,
             1.29207966e+01, 1.29470656e+01, 1.29733347e+01, 1.29996038e+01,
             1.30434980e+01, 1.30873922e+01, 1.31312864e+01, 1.31751806e+01,
             1.32190748e+01, 1.33125773e+01, 1.34060797e+01, 1.34995821e+01,
             1.35930846e+01, 1.36865870e+01, 1.38890130e+01, 1.40914391e+01,
             1.42938651e+01, 1.44962911e+01, 1.48659380e+01, 1.52355849e+01,
             1.72063049e+01, 1.91770248e+01, 2.11477447e+01,
             2.40000000e+01]), 'X': array(
            [0.01, 0.01000001, 0.01007442, 0.01027505, 0.01047923,
             0.01068731, 0.01101048, 0.01134339, 0.01194165, 0.01257137,
             0.01323421, 0.01437495, 0.01561403, 0.01695993, 0.02001104,
             0.02361154, 0.02785903, 0.03286946, 0.03878035, 0.04575387,
             0.05398109, 0.06368717, 0.07513765, 0.08864571, 0.10458067,
             0.12337794, 0.14555081, 0.17170425, 0.20255118, 0.23893152,
             0.26775043, 0.30003795, 0.33621059, 0.40167063, 0.45656932,
             0.51894332, 0.58980393, 0.67029632, 0.76171532, 0.86552457,
             0.98337771, 1.1171406, 1.26891467, 1.44106161, 1.63622853,
             1.99798087, 2.43767005, 2.7622085, 3.12812855, 3.53985117,
             3.84993488, 4.18478847, 4.54549087, 4.82397847, 5.11648553,
             5.42271114, 5.65601237, 5.89573243, 6.14096851, 6.39034286,
             6.56033205, 6.73039381, 6.89934182, 7.06561194, 7.22714514,
             7.38125988, 7.48380463, 7.5543561, 7.6207073, 7.68225962,
             7.73844325, 7.78877027, 7.832898, 7.87069075, 7.89349971,
             7.91335326, 7.93042318, 7.94492736, 7.95711585, 7.96725552,
             7.97561473, 7.98369653, 7.98839427, 7.99229022, 7.99550949,
             7.99816155, 8.00034043, 8.00212643, 8.00358754, 8.00530201,
             8.00656218, 8.00748644, 8.00816315, 8.00865792, 8.00901952,
             8.00928373, 8.0094769, 8.009618, 8.00972111, 8.0097963,
             8.00985127, 8.00989131, 8.0099207, 8.00994203, 8.00995777,
             8.00996906, 8.00997753, 8.00998398, 8.00998881, 8.00999209,
             8.0099942, 8.00999568, 8.00999685, 8.00999776, 8.00999839,
             8.0099988, 8.00999914, 8.00999925, 8.00999936, 8.00999958,
             8.00999978, 8.01000023, 8.01000049, 8.01000039, 8.01000014,
             8.00999999, 8.00999983, 8.00999989, 8.00999998, 8.01000001,
             8.01000002, 8.01000001, 8.01000001, 8.01, 8.01,
             8.01]), 'S_substrate': array(
            [2.00000000e+01, 2.00000000e+01, 1.99998140e+01, 1.99993124e+01,
             1.99988019e+01, 1.99982817e+01, 1.99974738e+01, 1.99966415e+01,
             1.99951459e+01, 1.99935716e+01, 1.99919145e+01, 1.99890626e+01,
             1.99859649e+01, 1.99826002e+01, 1.99749724e+01, 1.99659711e+01,
             1.99553524e+01, 1.99428263e+01, 1.99280491e+01, 1.99106153e+01,
             1.98900473e+01, 1.98657821e+01, 1.98371559e+01, 1.98033857e+01,
             1.97635483e+01, 1.97165551e+01, 1.96611230e+01, 1.95957394e+01,
             1.95186221e+01, 1.94276712e+01, 1.93556239e+01, 1.92749051e+01,
             1.91844735e+01, 1.90208234e+01, 1.88835767e+01, 1.87276417e+01,
             1.85504902e+01, 1.83492592e+01, 1.81207117e+01, 1.78611886e+01,
             1.75665557e+01, 1.72321485e+01, 1.68527133e+01, 1.64223460e+01,
             1.59344287e+01, 1.50300478e+01, 1.39308249e+01, 1.31194788e+01,
             1.22046786e+01, 1.11753721e+01, 1.04001628e+01, 9.56302883e+00,
             8.66127282e+00, 7.96505382e+00, 7.23378617e+00, 6.46822216e+00,
             5.88496908e+00, 5.28566893e+00, 4.67257871e+00, 4.04914285e+00,
             3.62416986e+00, 3.19901547e+00, 2.77664545e+00, 2.36097015e+00,
             1.95713716e+00, 1.57185031e+00, 1.31548844e+00, 1.13910974e+00,
             9.73231747e-01, 8.19350947e-01, 6.78891873e-01, 5.53074324e-01,
             4.42754998e-01, 3.48273128e-01, 2.91250720e-01, 2.41616847e-01,
             1.98942058e-01, 1.62681603e-01, 1.32210371e-01, 1.06861209e-01,
             8.59631646e-02, 6.57586866e-02, 5.40143186e-02, 4.42744583e-02,
             3.62262631e-02, 2.95961315e-02, 2.41489235e-02, 1.96839254e-02,
             1.60311546e-02, 1.17449793e-02, 8.59454568e-03, 6.28390615e-03,
             4.59212605e-03, 3.35519709e-03, 2.45120231e-03, 1.79067835e-03,
             1.30776192e-03, 9.55007216e-04, 6.97213900e-04, 5.09252537e-04,
             3.71823858e-04, 2.71722143e-04, 1.98247751e-04, 1.44928061e-04,
             1.05565573e-04, 7.73542359e-05, 5.61825443e-05, 4.00431335e-05,
             2.79801017e-05, 1.97696425e-05, 1.44933367e-05, 1.07997649e-05,
             7.87411266e-06, 5.60487745e-06, 4.03634962e-06, 3.00250108e-06,
             2.14584915e-06, 1.88743404e-06, 1.59825382e-06, 1.06207944e-06,
             5.43902318e-07, -5.74527374e-07, -1.22798991e-06, -9.68733873e-07,
             -3.40860531e-07, 1.53153067e-08, 4.18994832e-07, 2.87157290e-07,
             5.58479234e-08, -2.89640501e-08, -5.52070633e-08, -1.66479591e-08,
             -1.30759119e-08, -7.30389711e-10, 2.00891153e-10,
             5.95679793e-12]), 'P_product': array(
            [0.00000000e+00, 2.74886917e-09, 2.23258390e-05, 8.25140254e-05,
             1.43767584e-04, 2.06194151e-04, 3.03143993e-04, 4.03017093e-04,
             5.82495354e-04, 7.71411381e-04, 9.70263731e-04, 1.31248487e-03,
             1.68421018e-03, 2.08797802e-03, 3.00331127e-03, 4.08346290e-03,
             5.35770852e-03, 6.86083829e-03, 8.63410359e-03, 1.07261620e-02,
             1.31943273e-02, 1.61061506e-02, 1.95412948e-02, 2.35937144e-02,
             2.83742018e-02, 3.40133825e-02, 4.06652418e-02, 4.85112736e-02,
             5.77653536e-02, 6.86794565e-02, 7.73251291e-02, 8.70113850e-02,
             9.78631769e-02, 1.17501188e-01, 1.33970795e-01, 1.52682996e-01,
             1.73941180e-01, 1.98088897e-01, 2.25514595e-01, 2.56657370e-01,
             2.92013313e-01, 3.32142179e-01, 3.77674401e-01, 4.29318484e-01,
             4.87868560e-01, 5.96394260e-01, 7.28301016e-01, 8.25662550e-01,
             9.35438564e-01, 1.05895535e+00, 1.15198046e+00, 1.25243654e+00,
             1.36064726e+00, 1.44419354e+00, 1.53194566e+00, 1.62381334e+00,
             1.69380371e+00, 1.76571973e+00, 1.83929055e+00, 1.91410286e+00,
             1.96509962e+00, 2.01611814e+00, 2.06680255e+00, 2.11668358e+00,
             2.16514354e+00, 2.21137796e+00, 2.24214139e+00, 2.26330683e+00,
             2.28321219e+00, 2.30167789e+00, 2.31853298e+00, 2.33363108e+00,
             2.34686940e+00, 2.35820722e+00, 2.36504991e+00, 2.37100598e+00,
             2.37612695e+00, 2.38047821e+00, 2.38413476e+00, 2.38717665e+00,
             2.38968442e+00, 2.39210896e+00, 2.39351828e+00, 2.39468707e+00,
             2.39565285e+00, 2.39644846e+00, 2.39710213e+00, 2.39763793e+00,
             2.39807626e+00, 2.39859060e+00, 2.39896865e+00, 2.39924593e+00,
             2.39944894e+00, 2.39959738e+00, 2.39970586e+00, 2.39978512e+00,
             2.39984307e+00, 2.39988540e+00, 2.39991633e+00, 2.39993889e+00,
             2.39995538e+00, 2.39996739e+00, 2.39997621e+00, 2.39998261e+00,
             2.39998733e+00, 2.39999072e+00, 2.39999326e+00, 2.39999519e+00,
             2.39999664e+00, 2.39999763e+00, 2.39999826e+00, 2.39999870e+00,
             2.39999906e+00, 2.39999933e+00, 2.39999952e+00, 2.39999964e+00,
             2.39999974e+00, 2.39999977e+00, 2.39999981e+00, 2.39999987e+00,
             2.39999993e+00, 2.40000007e+00, 2.40000015e+00, 2.40000012e+00,
             2.40000004e+00, 2.40000000e+00, 2.39999995e+00, 2.39999997e+00,
             2.39999999e+00, 2.40000000e+00, 2.40000001e+00, 2.40000000e+00,
             2.40000000e+00, 2.40000000e+00, 2.40000000e+00, 2.40000000e+00])}
    )


@pytest.fixture
def placeholder_data():
    return pd.DataFrame({
        "time": [0.00000000e+00, 1.60350555e-06, 1.29272201e-02,
                 4.73210593e-02,
                 8.17148984e-02, 1.16108738e-01, 1.68220493e-01,
                 2.20332247e-01,
                 3.10246576e-01, 4.00160904e-01, 4.90075232e-01,
                 6.34757887e-01,
                 7.79440543e-01, 9.24123199e-01, 1.21353541e+00,
                 1.50294763e+00,
                 1.79235984e+00, 2.08177205e+00, 2.37118427e+00,
                 2.66059648e+00,
                 2.95000869e+00, 3.23942091e+00, 3.52883312e+00,
                 3.81824533e+00,
                 4.10765755e+00, 4.39706976e+00, 4.68648197e+00,
                 4.97589419e+00,
                 5.26530640e+00, 5.55471861e+00, 5.75429441e+00,
                 5.95387020e+00,
                 6.15344600e+00, 6.46543931e+00, 6.69021058e+00,
                 6.91498185e+00,
                 7.13975312e+00, 7.36452439e+00, 7.58929566e+00,
                 7.81406694e+00,
                 8.03883821e+00, 8.26360948e+00, 8.48838075e+00,
                 8.71315202e+00,
                 8.93792329e+00, 9.29231855e+00, 9.64671381e+00,
                 9.87042767e+00,
                 1.00941415e+01, 1.03178554e+01, 1.04707829e+01,
                 1.06237105e+01,
                 1.07766381e+01, 1.08876690e+01, 1.09986998e+01,
                 1.11097307e+01,
                 1.11913085e+01, 1.12728862e+01, 1.13544640e+01,
                 1.14360417e+01,
                 1.14912119e+01, 1.15463820e+01, 1.16015522e+01,
                 1.16567224e+01,
                 1.17118925e+01, 1.17670627e+01, 1.18060238e+01,
                 1.18344243e+01,
                 1.18628249e+01, 1.18912255e+01, 1.19196261e+01,
                 1.19480267e+01,
                 1.19764272e+01, 1.20048278e+01, 1.20247743e+01,
                 1.20447208e+01,
                 1.20646672e+01, 1.20846137e+01, 1.21045602e+01,
                 1.21245066e+01,
                 1.21444531e+01, 1.21685210e+01, 1.21859235e+01,
                 1.22033260e+01,
                 1.22207286e+01, 1.22381311e+01, 1.22555336e+01,
                 1.22729361e+01,
                 1.22903386e+01, 1.23166077e+01, 1.23428768e+01,
                 1.23691459e+01,
                 1.23954150e+01, 1.24216840e+01, 1.24479531e+01,
                 1.24742222e+01,
                 1.25004913e+01, 1.25267604e+01, 1.25530294e+01,
                 1.25792985e+01,
                 1.26055676e+01, 1.26318367e+01, 1.26581058e+01,
                 1.26843748e+01,
                 1.27106439e+01, 1.27369130e+01, 1.27631821e+01,
                 1.27894512e+01,
                 1.28157202e+01, 1.28419893e+01, 1.28682584e+01,
                 1.28945275e+01,
                 1.29207966e+01, 1.29470656e+01, 1.29733347e+01,
                 1.29996038e+01,
                 1.30434980e+01, 1.30873922e+01, 1.31312864e+01,
                 1.31751806e+01,
                 1.32190748e+01, 1.33125773e+01, 1.34060797e+01,
                 1.34995821e+01,
                 1.35930846e+01, 1.36865870e+01, 1.38890130e+01,
                 1.40914391e+01,
                 1.42938651e+01, 1.44962911e+01, 1.48659380e+01,
                 1.52355849e+01,
                 1.72063049e+01, 1.91770248e+01, 2.11477447e+01,
                 2.40000000e+01],
        "X": np.arange(136),
        "S_substrate": np.arange(136),
        "P_product": np.arange(136)
    })


@pytest.fixture
def parameters():
    return {
        "X_0": 0.01,
        "y_BM": 0.4,
        "S_substrate_km": 1,
        "S_substrate_qsmax": 1.5,
        "S_substrate_s_0": 20,
        "P_product_y_P": 0.12,
        "P_product_p_0": 0
    }


def test_monod_model(monod_model_sds, pyfoomb_simulated_data):
    """
    Test that the Monod model using pyFOOMB simulated data & parameters given
    as input.
    """

    io = physiofit.base.io.IoHandler()
    model = io.select_model(
        "Dynamic Monod model (1 substrate, 1 product)",
        pyfoomb_simulated_data
    )
    model.get_params()
    fitter = io.initialize_fitter(
        data=model.data,
        model=model,
        sd=monod_model_sds,
        debug_mode=True
    )
    fitter.optimize()
    optimized_params = {
        name: param for name, param in zip(
            list(fitter.model.parameters.keys()),
            fitter.parameter_stats["optimal"]
        )
    }

    assert np.allclose(
        b=list(optimized_params.values()),
        a=[0.01, 0.4, 1, 1.5, 20, 0.12, 0],
        rtol=1e-3,
        atol=1e-2
    )


def test_physiofit_simulations(parameters, placeholder_data,
                               pyfoomb_simulated_data):
    io = physiofit.base.io.IoHandler()
    model = io.select_model("Dynamic Monod model (1 substrate, 1 product)",
                            placeholder_data)
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
    df = df.reset_index()

    pd.testing.assert_frame_equal(
        df,
        pyfoomb_simulated_data,
        rtol=1e-3,
        atol=1e-2
    )
