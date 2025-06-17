// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;
 
// Base contract representing a simple bank account
contract BankAccount {
    // This variable stores the balance for each address
    mapping(address => uint256) private balances;
 
    // Function to deposit Ether into the account
    function deposit() public payable {
        // msg.value is the amount of Ether sent with the transaction
        balances[msg.sender] += msg.value;
    }
 
    // Function to check the balance of the caller's account
    function getBalance() public view returns (uint256) {
        // Return the balance of the address that called this function
        return balances[msg.sender];
    }
 
    // Internal function to allow derived contracts to access balances
    function _getInternalBalance(address user) internal view returns (uint256) {
        return balances[user];
    }
}
 
// Derived contract that adds interest calculation
contract SavingsAccount is BankAccount {
    uint256 public interestRate = 5; // Interest rate as a percentage (e.g., 5%)
 
    // Function to calculate interest based on the user's current balance
    function calculateInterest() public view returns (uint256) {
        // Get the balance using the internal function from the parent contract
        uint256 balance = _getInternalBalance(msg.sender);
 
        // Calculate interest: (balance * interestRate) / 100
        uint256 interest = (balance * interestRate) / 100;
 
        return interest;
    }
}