// some sample program for array and enums | Reading links at the end 
// SPDX-License-Identifier: GPL-3.0
 
pragma solidity >=0.7.0 <0.9.0;
 
 
//sample program for dynamic array
/*contract SimpleArray{
    uint[] public numbers;
    function addnumber(uint _num) public {
        numbers.push(_num);
    }
 
    function getNumber(uint _index) public  view returns (uint){
        return numbers[_index];
    }
}*/
 
//Simple program for fixed array
 
/*contract FixedArray{
    uint[3] public numbers = [10,20,20];
 
    function getnumber(uint _index) public view returns (uint){
        require((_index < 3),"index out of range");
        return numbers[_index];
    }
 
    function updateNumber(uint _index, uint _value)public {
        require(_index < 3, "index out of range");
        numbers[_index] = _value;
    }
}*/
//enum
contract Orderstatus{
    enum Status {pending , shipped, delivered, cancelled}
 
    Status public currentStatus;
 
    function setShipped() public {
        currentStatus = Orderstatus.Status.shipped;
    }
 
    function getStatus() public view returns (Status){
        return currentStatus;
    }
 
}
//enum
contract test{
    enum FreshJuiceSize{small, medium , large}
    FreshJuiceSize choice;
    FreshJuiceSize constant defaultChoice = FreshJuiceSize.medium;
 
    function setLarge() public {
        choice=FreshJuiceSize.large;
    }
   
    function getChoice() public view returns(FreshJuiceSize){
        return choice;
    }
 
    function getDefaultChoice() public pure returns (uint) {
        return uint(defaultChoice);
    }
}
 
 
// Reading sources : 
 
// https://www.tutorialspoint.com/solidity/solidity_arrays.htm
// https://www.geeksforgeeks.org/solidity-arrays/
// https://www.tutorialspoint.com/solidity/solidity_enums.htm
 
// Solidity Arrays Explained
// Solidity Arrays Explained - Discover the fundamentals of arrays in Solidity, including how to declare, initialize, and manipulate them effectively.
 