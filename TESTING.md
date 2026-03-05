\# Testing Strategy — Quick-Calc



\## Testing Strategy



This project follows a layered testing strategy to ensure both correctness of individual components and overall system behavior.



\### What was tested

\- Core arithmetic logic (addition, subtraction, multiplication, division)

\- Division by zero error handling

\- Negative number operations

\- Multiplication by zero

\- Full operation flow

\- Clear function reset behavior



\### What was not tested

\- Graphical user interface (not implemented)

\- Performance under heavy computational load

\- Security aspects

\- Cross-platform behavior



The focus was placed on functional correctness and reliability of the calculator logic.



---



\## Lecture Concepts



\### Testing Pyramid

The testing structure follows the Testing Pyramid principle:

\- Unit tests form the base layer (8 tests) verifying individual functions.

\- Integration tests form the middle layer (2 tests) validating combined behavior.

This ensures fast feedback and reliable system validation.



\### Black-box vs White-box Testing

\- Unit tests follow a white-box approach since internal logic and functions are directly tested.

\- Integration tests follow a black-box approach by validating behavior through function interactions.



\### Functional vs Non-Functional Testing

\- Functional testing was performed to ensure correct outputs for given inputs.

\- Non-functional testing such as performance and security testing was intentionally excluded due to scope.



\### Regression Testing

The test suite can be reused in future updates to detect regressions.

If new features or bug fixes introduce unexpected behavior, the existing tests will fail and alert developers.



---



\## Test Results Summary



| Test Name | Type | Status |

|----------|------|--------|

| Unit Tests (8) | Unit | Passed |

| Integration Tests (2) | Integration | Passed |

