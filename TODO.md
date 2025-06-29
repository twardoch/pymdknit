# TODO List for pymdknit

## Critical Priority

### Python Modernization
- [ ] Remove Python 2.7 support and py3compat.py module
- [ ] Replace all string formatting with f-strings
- [ ] Update exception handling to modern syntax
- [ ] Replace os.path with pathlib throughout codebase
- [ ] Remove encoding compatibility code, use UTF-8 everywhere

### Dependency Management
- [ ] Add all missing dependencies to setup.py
- [ ] Create requirements.txt and requirements-dev.txt
- [ ] Migrate from setup.py to pyproject.toml
- [ ] Update to latest versions of all dependencies
- [ ] Add version constraints for stability

### Bug Fixes
- [ ] Fix `include=False` with `eval=False` combination
- [ ] Fix base64 decoding issues
- [ ] Fix loop execution problems
- [ ] Fix pandoc table conversion bugs
- [ ] Fix filename-only path handling

## High Priority

### Error Handling
- [ ] Add line numbers to all error messages
- [ ] Create custom exception hierarchy
- [ ] Improve parser error messages
- [ ] Add validation for YAML headers
- [ ] Implement graceful error recovery

### Core Features
- [ ] Implement all basic chunk options (cache, fig.width, fig.height)
- [ ] Add support for chunk labels and references
- [ ] Complete implementation of results="hold"
- [ ] Fix comment option handling
- [ ] Add progress indicators for long documents

### Testing
- [ ] Increase test coverage to >90%
- [ ] Add integration tests for full document conversion
- [ ] Create tests for all output formats
- [ ] Add tests for error conditions
- [ ] Set up continuous integration with GitHub Actions

## Medium Priority

### Documentation
- [ ] Create comprehensive user guide
- [ ] Document all chunk options
- [ ] Write migration guide from knitr
- [ ] Add troubleshooting section
- [ ] Create API documentation

### Parser Improvements
- [ ] Rewrite parser to be line-based
- [ ] Add support for escaped code blocks
- [ ] Improve inline code detection
- [ ] Better handling of nested structures
- [ ] Add parser state validation

### Output Formats
- [ ] Refactor output handling to be pluggable
- [ ] Add Markdown output format
- [ ] Add reStructuredText output
- [ ] Implement custom templates
- [ ] Fix LaTeX output issues

## Low Priority

### Performance
- [ ] Implement chunk caching
- [ ] Add parallel execution option
- [ ] Optimize regex patterns
- [ ] Add memory usage limits
- [ ] Create benchmarking suite

### Advanced Features
- [ ] Add R kernel support
- [ ] Support for other Jupyter kernels
- [ ] Implement figure captioning
- [ ] Add table formatting options
- [ ] Create interactive widget support

### Developer Experience
- [ ] Create VS Code extension
- [ ] Add syntax highlighting for .pymd files
- [ ] Implement live preview
- [ ] Create project templates
- [ ] Add debugging tools

## Future Enhancements

### Distribution
- [ ] Set up automated PyPI releases
- [ ] Create Docker image
- [ ] Add conda-forge package
- [ ] Build standalone executables
- [ ] Create web service version

### Community
- [ ] Write contributing guidelines
- [ ] Set up issue templates
- [ ] Create discussion forum
- [ ] Find additional maintainers
- [ ] Create example gallery

### Nice to Have
- [ ] Add collaborative editing
- [ ] Implement version control integration
- [ ] Create cloud deployment option
- [ ] Add report scheduling
- [ ] Build plugin system for extensions