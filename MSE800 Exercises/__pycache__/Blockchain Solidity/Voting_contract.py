//voting smart contract 
// SPDX-License-Identifier: MIT
pragma solidity >=0.7.0 <0.9.0;
 
contract Voting{
    struct Vote{
        address receiver;
        uint256 timestamp;
 
    }
    mapping (address =>Vote) public votes;
    bool public voting; //declaring voting variable
    event AddVote(address indexed voter, address indexed receiver, uint256 timestemp);
 
    event RemoveVote(address indexed voter);
    event StartVoting(address indexed startedBy);
    event StopVoting(address indexed stoppedBy);
 
    constructor() {
        voting = false;
    }
    function startVoting() external returns(bool) {
        voting = true;
        emit StartVoting(msg.sender);
        return true;
    }
 
    function StopVoting() external returns(bool){
        voting = false;
        emit StopVoting(msg.sender);
        return true;
    }
 
    function AddVote(address receiver) external returns(bool) {
        require(voting, "voting is not active");
        votes[msg.sender] = Vote(receiver, block.timestamp);
        emit AddVote(msg.sender,receiver,block.timestamp);
        return true;
    }
 
    function RemoveVote() external returns(bool){
        require(voting,"voting is not active");
         delete votes[msg.sender];
         emit RemoveVote(msg.sender);
         return true;
    }
 
    function getVote(address voterAddress) external view returns (address candidateAddress){
        return votes[voterAddress].receiver;
    }
   
 
    }
}
 