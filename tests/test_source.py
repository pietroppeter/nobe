import pytest

from nobe.source import _cleanup

source_simple_lambda = """
nb.code(lambda: print("hi"))
"""

cleaned_simple_lambda = """
print("hi")
"""

source_simple_decorator = """
@nb.code
def _():
    print("hello")
"""

cleaned_simple_decorator = """
print("hello")
"""

# When inspect.getsource is called on a multi-line lambda,
# it returns the lambda expression itself (starting with "lambda: ").
# The _cleanup function should strip that prefix.
source_multiline_lambda = """\
    lambda: nb.image(
        url="https://example.com",
        alt="example image",
    )
"""

cleaned_multiline_lambda = """\
nb.image(
    url="https://example.com",
    alt="example image",
)"""

cleanup_test_data = [
    (source_simple_lambda, cleaned_simple_lambda),
    (source_simple_decorator, cleaned_simple_decorator),
    (source_multiline_lambda, cleaned_multiline_lambda),
]


@pytest.mark.parametrize("source, cleaned", cleanup_test_data)
def test_source_cleanup(source: str, cleaned: str):
    assert _cleanup(source) == cleaned.strip()
