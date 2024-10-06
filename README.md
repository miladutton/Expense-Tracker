# Expense Tracker

#### Description:

The Expense Tracker is a python application designed to help users manage their personal finances by tracking their expenses. This program allows users to add, view, and save their expenses efficiently.

### Features:

-   **Add Expenses**: Users can add expenses by specifying the category, amount, and date.

-   **View Summary**: This feature allows users to quickly see how much they have spent in each category.

-   **Save to CSV**: All entered expenses can be saved to a CSV file named `expense_tracker.csv`. This feature enables users to keep a record of their expenses for future reference.

### Design Choices:

I wanted this to be as straight forward and user friendly as possible. For that reason I chose to keep 3 simple fuctions. Fininacial management can be a daunting topic/task and I did not want this to be intimidating at all. It was important to me for the user to be able to track their spending habits over time as this can lead to more informed spending. Saving the data in a csv file seemed like the most straight forward way to allow the user to do so. Ideally the user can then further analyze their spending data using the software of their choice.

### Technologies Used:

-   **Python**: This application is built in python.
-   **CSV Module**: The built-in CSV module is used for saving and reading expense data.

### How to Use:

1.  Clone the repository or download the source code.
2.  Navigate to the project directory in your terminal.
3.  Run the application using the command `python project.py`.
4.  Follow the on-screen prompts to add, view, or save expenses.
5.  The expenses will be saved in a file called `expense_tracker.csv` in the same directory.

### Future Enhancements:

-   **User Authentication**: Implement user login functionality to allow multiple users to track their expenses securely.
-   **Data Visualization**: Integrate data visualization libraries (like Matplotlib or Seaborn) to provide graphical representations of spending patterns.
-   **Budgeting Features**: Allow users to set budgets for different categories and receive alerts when they exceed their limits.

### Conclusion:

I created the expense tracker for my final project in Harvard's CS50 intro to python programming course. It is a simple yet effective tool to help manage personal finances. Users can easily track how much money they are spending in a given category, as well as comparing their spending habits over time. With this information, the user can then make informed financial decisions thus leading to more optimized financial management.
