from conans import ConanFile, CMake

import os

class TinyProcessLibrary(ConanFile):
    name = 'tiny-process-library'
    url = 'https://github.com/sztomi/tiny-process-library'
    settings = 'os', 'compiler', 'build_type', 'arch'
    license = 'MIT'
    version = '1.0.5'
    exports = '*'
    generators = 'cmake'

    def build(self):
        cmake = CMake(self.settings)
        os.mkdir('build')
        os.chdir('build')
        self.run('cmake {} {} -DCMAKE_INSTALL_PREFIX={}'
                    .format(self.conanfile_directory,
                            cmake.command_line,
                            self.package_folder))
        self.run('cmake --build .')

    def package(self):
        self.copy('*.hpp', dst='include')
        self.copy('*.a', dst='lib', keep_path=False)
        self.copy('*.lib', dst='lib', keep_path=False)

    def package_info(self):
        self.cpp_info.libs = [self.name]
