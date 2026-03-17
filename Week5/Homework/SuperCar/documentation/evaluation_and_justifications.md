# Supercar Experience Calculator: Design, Implementation, and Evaluation Documentation

## Overview
This document provides a comprehensive justification and evaluation of the planning, design, and implementation decisions made in developing the Supercar Experience Calculator program. The program was created to meet the requirements of a local supercar experience company, allowing staff to calculate costs for customer experiences based on selected cars and additional laps.

**Program Details:**
- **File:** `supercarExperienceCalc.py`
- **Author:** Zachary Bhumgara
- **Date:** 2026
- **Language:** Python 3
- **Purpose:** Calculate and display itemized bills for supercar driving experiences

## Client Requirements
The program must allow staff to input:
- Customer details (name, address, phone number)
- Number of cars to drive (maximum 5)
- Specific car selections
- Number of additional laps (if any)

And provide:
- Personalized itemized bill with customer details
- Cost breakdown
- Total cost
- All currency values to two decimal places

## Design Decisions

### 1. Naming conventions
#### Decision:
Naming conventions would match that of the official Python style guide, PEP 8.
- **Variable names:** Use snake_case (all lowercase with words separated by underscores).
- **Constant names:** Use SCREAMING_SNAKE_CASE (all uppercase with words separated by underscores).
- **Function and Method Names:** Follow the same snake_case convention as variables, appended by an open and closing bracket containing any parameters `()`.
- Avoid using identifiers that reference the data type of the named object (i.e. use `CARS` not `DICTIONARY_CARS`). 

#### Justification:
- **Industry Standard:** PEP 8 (Python Enhancement Proposal 8) is the official Python style guide endorsed by the Python community and Guido van Rossum (Python's creator), making it the universally recognised standard.
- **Consistency & Readability:** Consistent naming patterns reduce cognitive load. Developers immediately understand that `CARS` is a constant and `get_customer_details()` is a function, without needing to search for variable declarations.
- **Recognition:** When working with other developers, following established conventions ensures code is immediately recognisable and maintainable by anyone familiar with Python.
- **Implementation Independence:** Using `CARS` instead of `DICTIONARY_CARS` decouples the variable name from its implementation detail. If the data structure changes (e.g., from dictionary to a list of tuples or a custom class), the variable name remains appropriate and code doesn't become misleading.
- **Semantic Clarity:** The name should describe *what* the data represents (cars available), not *how* it's implemented (as a dictionary). This focuses attention on the business logic rather than technical implementation details.

#### Evaluation:
**Strengths:**
- Universally recognised by Python developers, improving code readability and team collaboration.
- Clear semantic distinction between constants, variables, and functions.
- Implementation-agnostic; naming allows flexibility if data structures change.
**Weaknesses:**
- Requires constant vigilance and familiarity with the PEP 8 style guide.
- Requires consistent discipline across teams.
**Overall:**
- Essential best practice that significantly enhances code quality and maintainability.

### 2. Modular Function-Based Structure
#### Decision:
The program is organized into multiple functions, each handling a specific aspect of the application (e.g., `display_welcome()`, `get_customer_details()`, `calculate_costs()`, `display_bill()`).

#### Justification:
- Follows the principle of separation of concerns, making the code more readable and maintainable.
- Allows for easier testing and debugging of individual components.
- Promotes code reusability - functions can be called independently if needed.
- Aligns with Python best practices and PEP 8 conventions.

#### Evaluation:
**Strengths:** 
- Highly maintainable; changes to one feature don't affect others (e.g. alterations to `calculate_costs()` won't change `display_welcome()`).
- Easy to understand program flow.
- High reusability: Code blocks allow for future reuse and expansion of features; such that, if customers want to place multiple orders they may reuse the `get_number_of_cars()` and `get_car_choices()` code blocks.
**Weaknesses:** 
- Slightly more verbose than a single linear program.
**Overall:**
- Excellent decision that enhances long-term code quality.

### 3. Data Structures and Constants
#### Decision:
Car prices stored in a constant dictionary (`CARS`), with pricing constants defined at the top of the file.

#### Justification:
- Dictionary provides O(1) lookup time for car prices, which is efficient for the small dataset.
- Constants are easily configurable and cannot be altered by the user.
- Avoids "magic numbers" scattered throughout the code.
- Dictionary keys use lowercase strings for consistency and easy comparison.

#### Evaluation:
**Strengths:**
- Highly efficient and maintainable. Easy to add/remove cars or update prices.
**Weaknesses:**
- None significant for this scale; could be moved to a configuration file for larger applications.
**Overall:**
- Optimal choice for the requirements.

### 4. User Interface Design
#### Decision:
Console-based interface with formatted text output using borders, centering, and aligned columns.

#### Justification:
- Simple and appropriate for a staff tool in a business environment.
- No external dependencies required (pure Python).
- Professional appearance with clear sections for different inputs.
- Meets the requirement for a "personalised and itemised bill" with comprehensive information display.

#### Evaluation:
**Strengths:**
- User-friendly with clear prompts and error messages. Professional output formatting.
**Weaknesses:**
- Limited to console; no GUI or file export capabilities (not required by client).
**Overall:**
- Well-suited to the target users and requirements.

## Implementation Decisions

### 1. Language Choice
#### Decision:
Python 3

#### Justification:
- Excellent string handling and formatting capabilities (f-strings, string methods).
- Built-in input/output functions suitable for console applications.
- Cross-platform compatibility.
- Readable syntax ideal for educational and professional development.
- Strong community support and extensive standard library.
- Easy to pick-up for new developers, making it easier to maintain.

#### Evaluation:
**Strengths:**
- Perfect match for the task; no performance issues for this application type.
**Weaknesses:**
- None; could be implemented in other languages, but Python is ideal here.
**Overall:**
- Excellent choice.

### 2. Input Validation and Error Handling
#### Decision:
Comprehensive validation using while loops and try-except blocks.

#### Justification:
- Prevents invalid data from causing program crashes or incorrect calculations.
- Provides clear, user-friendly error messages.
- Handles common input errors (empty strings, non-numeric input, out-of-range values).
- Ensures data integrity before processing.

#### Evaluation:
**Strengths:**
- Robust and user-friendly; prevents most runtime errors.
- Includes some advanced validation of phone numbers, ensuring phone number format is met.
**Weaknesses:**
- Could include more advanced validation (e.g., address format checking), but sufficient for requirements.
**Overall:**
- Strong implementation that enhances reliability.

### 3. Calculation Logic
#### Decision:
Straightforward arithmetic operations with detailed cost breakdowns.

#### Justification:
- Simple, transparent calculations that are easy to verify.
- Returns multiple values from `calculate_costs()` for detailed reporting.
- Handles both car costs and additional lap costs separately.
- Ensures all currency values display to exactly two decimal places.

#### Evaluation:
**Strengths:**
- Accurate, efficient, and transparent. Meets all calculation requirements.
**Weaknesses:**
- No complex pricing rules (e.g., discounts), but not required.
**Overall:**
- Perfect for the scope.

## Overall Evaluation

### Strengths
- **Requirement Compliance:** Fully meets all client specifications.
- **User-Friendliness:** Clear interface with helpful prompts and error messages.
- **Robustness:** Strong input validation prevents common errors.
- **Accuracy:** Precise calculations with proper currency formatting.
- **Maintainability:** Modular design and clean code following standards.
- **Efficiency:** Performs well for its intended use case.

### Weaknesses
- **Testing:** Limited to manual testing; lacks automated unit tests.
- **Features:** No advanced capabilities (e.g., data persistence, file output).
- **Scalability:** Designed for console use; may need adaptation for web/mobile.
- **Edge Cases:** Could handle more input validation scenarios.

### Recommendations for Improvement
1. **Testing:** Implement unit tests for individual functions.
2. **Features:** Add file output (e.g., save bills to text/PDF files).
3. **Validation:** Enhance input checking (e.g., address formats, prevent duplicate car selections).
4. **Configuration:** Move car data to an external file for easier maintenance.
5. **Error Handling:** Add logging for debugging in production use.

### Conclusion
The Supercar Experience Calculator demonstrates programming practices appropriate for its requirements, maintaining use of standard programming conventions. The design and implementation decisions result in a reliable, user-friendly program that effectively serves the client's needs. While there are opportunities for enhancement, the current solution is well-suited for its intended business context.

**Final Assessment:** The program successfully balances functionality, usability, and code quality, making it a well-suited for current use-cases.