//Inheritance 
// SPDX-License-Identifier: GPL-3.0
 
pragma solidity >=0.7.0 <0.9.0;
// program for inheritance
/*contract animal{
    string public name;
    function setName(string memory _name) public {
        name = _name;
    }
    function speak() public view returns (string memory){
        return string(abi.encodePacked(name,"makes a sound"));
    }
}
// child contract
contract Dog is animal{
    function bark() public view returns (string memory) {
        return string(abi.encodePacked(name,"says woof!"));
    }
}*/
 
//single level inheritance
 
/*contract A {
    function sayHello() public pure returns (string memory) {  
        return "hello from A";
    }
}
 
contract B is A{
    //inherits sayhello() from A
}*/
 
// multi level inheritance
 
/*contract A{
    function greet() public pure returns (string memory) {
        return "hi from A";
    }  
}
contract B is A {
    function sayHi() public pure returns (string memory) {
        return "hi from B";    
    }
}
contract C is B {
    function sayWelcome() public pure returns (string memory) {
        return "welcome from c";
    }
}*/
 
//Multiple inheritance
 
contract A {
    function getA() public pure  returns (string memory) {
        return "this is A";
 
    }
}
contract B{
    function getB() public pure returns(string memory){
        return "this is B";
    }
}
contract C is A, B{
    function getC() public pure returns (string memory) {
        return " this is C ";
    }
}
 