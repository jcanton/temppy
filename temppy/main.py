
class FooClass():

    def __init__(self):

        self.a = 0
        self.b = 10
        self.c = 20
        self.d = 30

    def fooMethod(self):
        """
        This is the foo method

        This is its main docstring

        Args:
            arg1 (type1): The first argument
            arg2 (type2): The second argument
        """

        self.a += 1

        """
        docstring 2

        Args:
            barg1 (type1): The first bargument
            barg2 (type2): The second bargument
        """

        self.b += 1

        """
        This docstring shows off math
        (https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-math),
        with both inline :math:`a^2+b^2=c^2` and block math (white lines are important):

        .. math:: e^{i\pi} + 1 = 0
            :label: euler

        Which can also be labelled and referenced as: equation
        :math:numref:`euler`, which was elected one of the most beautiful
        mathematical formulas.
        Multiline works too

        .. math::
            :label: euler2

            e^{i\pi} + 1 = 0 \\
            e^{j\pi} + 2 = 0
        
        Then we should try $e^{i\pi} + 1 = 0$ inline math with dollars as well as block math with dollars

        $$
        e^{i\pi} + 1 = 0 \\
        e^{j\pi} + 2 = 0
        $$ (euler3)

        which maybe can be referenced as {eq}`euler3`.

        $$
        (a + b)^2 = a^2 + 2ab + b^2
        $$

        The equation {eq}`mymath` is a quadratic equation.

        """

        self.c += 1

        """
        This docstring shows off code blocks
        (https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-sourcecode)
        (white lines are important here too):

        .. code-block:: python

            z_exner_ex_pr = (1 + exner_exfac) * (exner - exner_ref_mc) - exner_exfac * exner_pr
        """

        self.d += 1

        """
        And finally references to other methods such as :meth:`barMethod`
        """


    def barMethod(self):
        """
        Just an empty method to reference
        """
        pass