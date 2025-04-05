from unittest.mock import Mock

from pydantic import ValidationError
import pytest
from atendimento import Atendimento


def test_validar_predio__predio_1__expected_predio_1():
    # Fixture
    atendimento_mock = Mock(spec=Atendimento)
    atendimento_mock.predio = "1"
    atendimento_mock.validar_predio = Atendimento.validar_predio

    # Exercise
    predio = atendimento_mock.validar_predio(atendimento_mock.predio)

    # Assert
    assert predio == "1"


def test_validar_predio__predio_2__expected_predio_2():
    # Fixture
    atendimento_mock = Mock(spec=Atendimento)
    atendimento_mock.predio = "2"
    atendimento_mock.validar_predio = Atendimento.validar_predio

    # Exercise
    predio = atendimento_mock.validar_predio(atendimento_mock.predio)

    # Assert
    assert predio == "2"


def test_validar_predio__predio_3__expected_predio_3():
    # Fixture
    atendimento_mock = Mock(spec=Atendimento)
    atendimento_mock.predio = "3"
    atendimento_mock.validar_predio = Atendimento.validar_predio

    # Exercise
    predio = atendimento_mock.validar_predio(atendimento_mock.predio)

    # Assert
    assert predio == "3"


def test_validar_predio__predio_5__expected_error():
    # Fixture
    atendimento_mock = Mock(spec=Atendimento)
    atendimento_mock.validar_predio = Atendimento.validar_predio
    atendimento_mock.predio = "5"

    # Exercise and Assert
    try:
        atendimento_mock.validar_predio(atendimento_mock.predio)
    except ValueError as e:
        assert str(e) == "O prédio deve ser '1', '2', '3', '4' ou '6'"


def test_validar_predio__predio_10__expected_error():
    # Fixture
    atendimento_mock = Mock(spec=Atendimento)
    atendimento_mock.validar_predio = Atendimento.validar_predio
    atendimento_mock.predio = "10"

    # Exercise and Assert
    try:
        atendimento_mock.validar_predio(atendimento_mock.predio)
    except ValueError as e:
        assert str(e) == "O prédio deve ser '1', '2', '3', '4' ou '6'"


def test_validar_predio__predio_50__expected_error():
    # Fixture
    atendimento_mock = Mock(spec=Atendimento)
    atendimento_mock.validar_predio = Atendimento.validar_predio
    atendimento_mock.predio = "50"

    # Exercise and Assert
    try:
        atendimento_mock.validar_predio(atendimento_mock.predio)
    except ValueError as e:
        assert str(e) == "O prédio deve ser '1', '2', '3', '4' ou '6'"


def test_get_predio__sala_1__expected_predio_1():
    # Fixture
    atendimento_mock = Mock(spec=Atendimento)
    atendimento_mock.get_predio = Atendimento.get_predio
    atendimento_mock.sala = 1

    # Exercise
    predio = atendimento_mock.get_predio(atendimento_mock)

    # Assert
    assert predio == "1"


def test_get_predio__sala_6__expected_predio_2():
    # Fixture
    atendimento_mock = Mock(spec=Atendimento)
    atendimento_mock.get_predio = Atendimento.get_predio
    atendimento_mock.sala = 6

    # Exercise
    predio = atendimento_mock.get_predio(atendimento_mock)

    # Assert
    assert predio == "2"


def test_get_predio__sala_12__expected_predio_3():
    # Fixture
    atendimento_mock = Mock(spec=Atendimento)
    atendimento_mock.get_predio = Atendimento.get_predio
    atendimento_mock.sala = 12

    # Exercise
    predio = atendimento_mock.get_predio(atendimento_mock)

    # Assert
    assert predio == "3"


def test_get_predio__sala_16__expected_predio_4():
    # Fixture
    atendimento_mock = Mock(spec=Atendimento)
    atendimento_mock.get_predio = Atendimento.get_predio
    atendimento_mock.sala = 16

    # Exercise
    predio = atendimento_mock.get_predio(atendimento_mock)

    # Assert
    assert predio == "4"


def test_get_predio__sala_21__expected_predio_6():
    # Fixture
    atendimento_mock = Mock(spec=Atendimento)
    atendimento_mock.get_predio = Atendimento.get_predio
    atendimento_mock.sala = 21

    # Exercise
    predio = atendimento_mock.get_predio(atendimento_mock)

    # Assert
    assert predio == "6"


def test_get_predio__sala_26__expected_error():
    # Fixture
    atendimento_mock = Mock(spec=Atendimento)
    atendimento_mock.get_predio = Atendimento.get_predio
    atendimento_mock.sala = 26

    # Exercise and Assert
    try:
        atendimento_mock.get_predio(atendimento_mock)
    except ValueError as e:
        assert str(e) == "Prédio não encontrado"


def test_get_predio__sala_39__expected_error():
    # Fixture
    atendimento_mock = Mock(spec=Atendimento)
    atendimento_mock.get_predio = Atendimento.get_predio
    atendimento_mock.sala = 39

    # Exercise and Assert
    try:
        atendimento_mock.get_predio(atendimento_mock)
    except ValueError as e:
        assert str(e) == "Prédio não encontrado"


def test_get_predio__sala_999__expected_error():
    # Fixture
    atendimento_mock = Mock(spec=Atendimento)
    atendimento_mock.get_predio = Atendimento.get_predio
    atendimento_mock.sala = 999

    # Exercise and Assert
    try:
        atendimento_mock.get_predio(atendimento_mock)
    except ValueError as e:
        assert str(e) == "Prédio não encontrado"


def test_get_predio__sala_321__expected_error():
    # Fixture
    atendimento_mock = Mock(spec=Atendimento)
    atendimento_mock.get_predio = Atendimento.get_predio
    atendimento_mock.sala = 321

    # Exercise and Assert
    try:
        atendimento_mock.get_predio(atendimento_mock)
    except ValueError as e:
        assert str(e) == "Prédio não encontrado"


def test_periodo__valor_valido_integral__expected_success():
    # Fixture & Exercise
    atendimento = Atendimento(
        nome_professor="Chris", horario="17:30-19:10", periodo="integral", sala=3
    )

    # Assert
    assert atendimento.periodo == "integral"


def test_periodo__valor_valido_noturno__expected_success():
    # Fixture & Exercise
    atendimento = Atendimento(
        nome_professor="Chris", horario="17:30-19:10", periodo="noturno", sala=3
    )

    # Assert
    assert atendimento.periodo == "noturno"


def test_periodo__valor_invalido_manha__expected_validation_error():
    # Fixture
    periodo_invalido = "manha"

    # Exercise & Assert
    with pytest.raises(ValidationError) as e:
        Atendimento(
            nome_professor="Chris",
            horario="17:30-19:10",
            periodo=periodo_invalido,
            sala=3,
        )

    assert "Input should be 'integral' or 'noturno'" in str(e.value)


def test_periodo__valor_invalido_tarde__expected_validation_error():
    # Fixture
    periodo_invalido = "tarde"

    # Exercise & Assert
    with pytest.raises(ValidationError) as e:
        Atendimento(
            nome_professor="Chris",
            horario="17:30-19:10",
            periodo=periodo_invalido,
            sala=3,
        )

    assert "Input should be 'integral' or 'noturno'" in str(e.value)


def test_periodo__valor_invalido_noite__expected_validation_error():
    # Fixture
    periodo_invalido = "noite"

    # Exercise & Assert
    with pytest.raises(ValidationError) as e:
        Atendimento(
            nome_professor="Chris",
            horario="17:30-19:10",
            periodo=periodo_invalido,
            sala=3,
        )

    assert "Input should be 'integral' or 'noturno'" in str(e.value)
