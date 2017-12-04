from conans import ConanFile, tools


class BoostConcept_CheckConan(ConanFile):
    name = "Boost.Concept_Check"
    version = "1.65.1"
    requires = "Boost.Level5Group/1.65.1@bincrafters/testing"
    lib_short_names = ["concept_check"]
    is_header_only = True
    is_in_cycle_group = True

    # BEGIN

    url = "https://github.com/bincrafters/conan-boost-concept_check"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    short_paths = True
    build_requires = "Boost.Generator/1.65.1@bincrafters/testing"

    def package_id(self):
        self.info.header_only()

    @property
    def env(self):
        try:
            with tools.pythonpath(super(self.__class__, self)):
                import boostgenerator  # pylint: disable=F0401
                boostgenerator.BoostConanFile(self)
        except:
            pass
        return super(self.__class__, self).env

    # END
