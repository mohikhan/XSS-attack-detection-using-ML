# XSS-Attack-ML

A lightweight and super fast C/C++ library for sequence alignment using [edit distance](https://en.wikipedia.org/wiki/Edit_distance).

Calculating edit distance of two strings is as simple as:
```c
edlibAlign("hello", 5, "world!", 6, edlibDefaultAlignConfig()).editDistance;
```

Edlib is also available for **Python** [![PyPI version](https://img.shields.io/pypi/v/edlib.svg) (Click here for Python README)](https://pypi.python.org/pypi/edlib), with code residing at [bindings/python](bindings/python).

Developers have created bindings to edlib in other languages as well:

* [Edlib.jl](https://github.com/cjdoris/Edlib.jl), a Julia package created and supported by Christopher Rowley ([@cjdoris](https://github.com/cjdoris))
* [edlibR](https://github.com/evanbiederstedt/edlibr), an R package created and supported by Evan Biederstedt ([@evanbiederstedt](https://github.com/evanbiederstedt))

## Features
* Calculates **edit distance (Levenshtein distance)**.
* It can find **optimal alignment path** (instructions how to transform first sequence into the second sequence).
* It can find just the **start and/or end locations of alignment path** - can be useful when speed is more important than having exact alignment path.
* Supports **multiple [alignment methods](#alignment-methods)**: global(**NW**), prefix(**SHW**) and infix(**HW**), each of them useful for different scenarios.
* You can **extend character equality definition**, enabling you to e.g. have wildcard characters, to have case insensitive alignment or to work with degenerate nucleotides.
* It can easily handle small or **very large sequences**, even when finding alignment path, while consuming very little memory.
* **Super fast** thanks to Myers's bit-vector algorithm.

## Using Edlib in your project
You can use Edlib in you project by either directly copying header and source files from [edlib/](edlib/), or by linking Edlib library (see [Building](#building) for instructions how to build Edlib libraries).
In any case, only thing that you have to do in your source files is to include `edlib.h`.

To get you started quickly, let's take a look at a few ways to get simple Hello World project working.

Our Hello World project has just one source file, `helloWorld.cpp` file, and it looks like this:
```cpp
#include <cstdio>
#include "edlib.h"

int main() {
    EdlibAlignResult result = edlibAlign("hello", 5, "world!", 6, edlibDefaultAlignConfig());
    if (result.status == EDLIB_STATUS_OK) {
        printf("edit_distance('hello', 'world!') = %d\n", result.editDistance);
    }
    edlibFreeAlignResult(result);
}
```

Running it should output `edit_distance('hello', 'world!') = 5`.

### Approach #1: Directly copying edlib source and header files.
Here we directly copied [edlib/](edlib/) directory to our project, to get following project structure:
```
edlib/  -> copied from edlib/
  include/
    edlib.h
  src/
    edlib.cpp
helloWorld.cpp -> your program
```

Since `helloWorld` is a c++ program, we can compile it with just one line: `c++ helloWorld.cpp edlib/src/edlib.cpp -o helloWorld -I edlib/include`.

If hello world was a C program, we would compile it like this:
```
    c++ -c edlib/src/edlib.cpp -o edlib.o -I edlib/include
    cc -c helloWorld.c -o helloWorld.o -I edlib/include
    c++ helloWorld.o edlib.o -o helloWorld
```

### Approach #2: Copying edlib header file and static library.
Instead of copying edlib source files, you could copy static library (check [Building](#building) on how to create static library). We also need to copy edlib header files. We get following project structure:
```
edlib/  -> copied from edlib
  include/
    edlib.h
  edlib.a
helloWorld.cpp -> your program
```

Now you can compile it with `c++ helloWorld.cpp -o helloWorld -I edlib/include -L edlib -ledlib`.

### Approach #3: Install edlib library on machine.
Alternatively, you could avoid copying any Edlib files and instead install libraries by running `sudo make install` (check [Building](#building) for exact instructions depending on approach you used for building). Now, all you have to do to compile your project is `c++ helloWorld.cpp -o helloWorld -ledlib`.
If you get error message like `cannot open shared object file: No such file or directory`, make sure that your linker includes path where edlib was installed.

### Approach #4: Use edlib in your project via CMake.
#### Using git submodule
If you are using CMake for compilation, we suggest adding edlib as a git submodule with the command `git submodule add https://github.com/martinsos/edlib vendor/edlib`. Afterwards, modify your top level CMakeLists.txt file accordingly:
```
add_subdirectory(vendor/edlib EXCLUDE_FROM_ALL)
target_link_libraries(your_exe edlib) # or target_link_libraries(your_exe edlib)
```
The `add_subdirectory` command adds a folder to the build tree, meaning it will run CMakeLists.txt from the included folder as well. Flag `EXCLUDE_FROM_ALL` disables building (and instalment) of targets in the added folder which are not needed in your project. In the above example only the (static) library `edlib` will be build, while `edlib-aligner`, `hello_world` and the rest won't. In order to access the `edlib` API, add `#include "edlib.h"` in your source file (CMake will automatically update your include path).


For more example projects take a look at applications in [apps/](apps/).

#### Using VCPKG
Edlib is available on [VCPKG](https://github.com/microsoft/vcpkg) package manager. With VCPKG on your system, Edlib can be downloaded using the VCPKG install command `vcpkg install edlib`. Once the library has been downloaded, add the following instructions to your CMakeLists.txt file:
```
find_package(edlib CONFIG REQUIRED)
target_link_libraries(MyProject PRIVATE edlib::edlib)
```

then you should be able to include the library header in your project (`#include "edlib.h`)


## Building
### Meson
Primary way of building Edlib is via [Meson](https://mesonbuild.com/) build tool.

Requirements: make sure that you have `meson` installed on your system.

Execute
```
make
```
to build **static** library and binaries (apps and tests) and also run tests.  
To build **shared** library and binaries, do `make LIBRARY_TYPE=shared`.

Library and binaries will be created in `meson-build` directory.  
You can choose alternate build directory like this: `make BUILD_DIR=some-other-dir`.

Optionally, you can run
```
sudo make install
```
to install edlib library on your machine (on Linux, this will usually install it to `usr/local/lib` and `usr/local/include`).

Check Makefile if you want to run individual steps on your own (building, tests, ...).

NOTE: If you need more control, use `meson` command directly, `Makefile` is here only to help with common commands.

### CMake
Edlib can alternatively be built with CMake.

Execute following command to build Edlib using CMAKE:
```
cd build && cmake -D CMAKE_BUILD_TYPE=Release .. && make
```
This will create binaries in `bin/` directory and libraries (static and shared) in `lib/` directory.

```
./bin/runTests
```
to run tests.

Optionally, you can run
```
sudo make install
```
to install edlib library on your machine.

### Conda
Edlib can also be installed via Conda: [![Anaconda-Server Badge](https://anaconda.org/bioconda/edlib/badges/installer/conda.svg)](https://conda.anaconda.org/bioconda): `conda install edlib`.


## Usage and examples
Main function in edlib is `edlibAlign`. Given two sequences (and their lengths), it will find edit distance, alignment path or its end and start locations.

```c
char* query = "ACCTCTG";
char* target = "ACTCTGAAA"
EdlibAlignResult result = edlibAlign(query, 7, target, 9, edlibDefaultAlignConfig());
if (result.status == EDLIB_STATUS_OK) {
    printf("%d", result.editDistance);
}
edlibFreeAlignResult(result);
```

NOTE: One character is expected to occupy one char/byte, meaning that characters spanning multiple chars/bytes are not supported. As long as your alphabet size is <= 256 you can manually map it to numbers/chars from 0 to 255 and solve this that way, but if its size is > 256 then you will not be able to use Edlib.

### Configuring edlibAlign()
`edlibAlign` takes configuration object (it is a struct `EdlibAlignConfig`), which allows you to further customize how alignment will be done. You can choose [alignment method](#alignment-methods), tell edlib what to calculate (just edit distance or also path and locations) and set upper limit for edit distance.

For example, if you want to use infix(HW) alignment method, want to find alignment path (and edit distance), are interested in result only if edit distance is not larger than 42 and do not want to extend character equality definition, you would call it like this:
```c
edlibAlign(seq1, seq1Length, seq2, seq2Length,
           edlibNewAlignConfig(42, EDLIB_MODE_HW, EDLIB_TASK_PATH, NULL, 0));
```
Or, if you want to use suffix(SHW) alignment method, want to find only edit distance, do not have any limits on edit distance and want character '?' to match both itself and characters 'X' and 'Y', you would call it like this:
```c
EdlibEqualityPair additionalEqualities[2] = {{'?', 'X'}, {'?', 'Y'}};
edlibAlign(seq1, seq1Length, seq2, seq2Length,
           edlibNewAlignConfig(-1, EDLIB_MODE_SHW, EDLIB_TASK_DISTANCE, additionalEqualities, 2));
```

We used `edlibNewAlignConfig` helper function to easily create config, however we could have also just created an instance of it and set its members accordingly.

### Handling result of edlibAlign()
`edlibAlign` function returns a result object (`EdlibAlignResult`), which will contain results of alignment (corresponding to the task that you passed in config).

```c
EdlibAlignResult result = edlibAlign(seq1, seq1Length, seq2, seq2Length,
                                     edlibNewAlignConfig(-1, EDLIB_MODE_HW, EDLIB_TASK_PATH, NULL, 0));
if (result.status == EDLIB_STATUS_OK) {
    printf("%d\n", result.editDistance);
    printf("%d\n", result.alignmentLength);
    printf("%d\n", result.endLocations[0]);
}
edlibFreeAlignResult(result);
```

It is important to remember to free the result object using `edlibFreeAlignResult` function, since Edlib allocates memory on heap for certain members. If you decide to do the cleaning manually and not use `edlibFreeAlignResult`, do not forget to manually `free()` required members.

### Turning alignment to cigar
Cigar is a standard way to represent alignment path.
Edlib has helper function that transforms alignment path into cigar.
```c
char* cigar = edlibAlignmentToCigar(result.alignment, result.alignmentLength, EDLIB_CIGAR_STANDARD);
printf("%s", cigar);
free(cigar);
```

## API documentation

For complete documentation of Edlib library API, visit [http://martinsos.github.io/edlib](https://martinsos.github.io/edlib) (should be updated to the latest release).

To generate the latest API documentation yourself from the source, you need to have [doxygen](www.doxygen.org) installed.
Position yourself in the root directory and run `doxygen`, this will generate `docs/` directory. Then open `docs/html/index.html` file with you favorite browser.

Alternatively, you can directly check [edlib.h](edlib/include/edlib.h).

## Running tests
Check [Building](#building) to see how to build binaries (including binary `runTests`).
To run tests, just run `./runTests`. This will run random tests for each alignment method, and also some specific unit tests.


## Time and space complexity
Edlib is based on [Myers's bit-vector algorithm](http://www.gersteinlab.org/courses/452/09-spring/pdf/Myers.pdf) and extends from it.
It calculates a dynamic programming matrix of dimensions `Q x T`, where `Q` is the length of the first sequence (query), and `T` is the length of the second sequence (target). It uses Ukkonen's banded algorithm to reduce the space of search, and there is also parallelization from Myers's algorithm, however time complexity is still quadratic.
Edlib uses Hirschberg's algorithm to find alignment path, therefore space complexity is linear.

Time complexity: `O(T * Q)`.

Space complexity: `O(T + Q)`.

It is worth noting that Edlib works best for large, similar sequences, since such sequences get the highest speedup from banded approach and bit-vector parallelization.


## Test data
In [test_data/](test_data) directory there are different genome sequences, ranging from 10 kbp to 5 Mbp in length. They are ranging in length and similarity, so they can be useful for testing and measuring speed in different scenarios.