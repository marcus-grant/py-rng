# Python Random Number Generation Utilities

I have a fascination with [Claude Shannon][2](https://en.wikipedia.org/wiki/Claude_Shannon)'s and other great thinkers like him's works on [information theory][1]. I also have some *(possibly)* nifty ideas about personal information security. So I've decided to combine all of my works in personal cryptogoraphy and entropy into this one repository of scripts, apps, configurations, console utilites, embedded systems, and analysis notebooks on the subject here. Feel free to use and **constructively peer review** my findings. I'm a self taught software engineer and a university taught electrical engineer, so although I have a decent academic experience and intregue in this field, I would love feedback on anything I find here.

## Contents

**TBD**

## TODO
- [x] Generate reasonably secure OS-sourced random numbers
- [x] Create random wordlist strings
- [x] Create ongoing jupyter notebook covering the analysis of utilities
- [ ] Compute basic statistics on random numbers
- [ ] Add proper [exception handling][10] for rng.py
- [ ] Add proper exception handling for random_words.py
- [ ] Refactor rng.py to be more functional
- [ ] Make rng.py into a proper python module, with OS integration
- [ ] Create PRNG wordlist terminal utility using modules here
  - [ ] Try a Rust or C version? Worth it? Maybe to learn Rust?
- [ ] Create proper unit tests
- [ ] Create evaluations module to test randomness
- [ ] Test wordlist strings
- [ ] Create submodule and package wordlist tools as wordly
- [ ] CUDA acceleration
- [ ] OpenCL acceleration
- [ ] Create module to generate wordlists
- [ ] Take notes on things learned for blog
- [ ] Create option to generate random numbers from external hardware
- [ ] Create a script that encrypts the wordlists folder
- [ ] Integrate scripts, modules, configs & files integrate better into OS
- [ ] Create an arduino/AVR based hardware RNG
  - [ ] Design circuit to generate entropy
  - [ ] Test circuit for randomness
  - [ ] Design & iterate PCB design for performance, versatility, size, io
  - [ ] Write AVR/arduino firmware to output entropy through...
    - [ ] USB
    - [ ] UART
    - [ ] SPI
    - [ ] i2c
  - [ ] Design a version for portable generation & display of randomness
  - [ ] Create python driver for module
  - [ ] Create C driver for module???
  - [ ] Create Unit tests for everything

## References
[1]: https://en.wikipedia.org/wiki/Information_theory
- [Wikipedia: Information Theory][1]
[2]: https://en.wikipedia.org/wiki/Claude_Shannon
- [Wikipedia: Claude Shannon][2]
[10]: https://www.programiz.com/python-programming/exception-handling "Tutorial on Py Exception"
- [Python Exception Handling][10]
