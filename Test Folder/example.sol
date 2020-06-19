pragma solidity >=0.4.22 <0.7.0;

contract example {

  address contractOwner;

  function example2() public {
    contractOwner = msg.sender;
  }
}