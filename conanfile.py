#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/stable")

class BoostConcept_CheckConan(base.BoostBaseConan):
    name = "boost_concept_check"
    url = "https://github.com/bincrafters/conan-boost_concept_check"
    lib_short_names = ["concept_check"]
    header_only_libs = ["concept_check"]
    b2_requires = [
        "boost_config",
        "boost_mpl",
        "boost_preprocessor",
        "boost_type_traits"
    ]


