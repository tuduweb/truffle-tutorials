// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract NameContract{
    string public name = "DNA";
    
    function getName() public view returns(string memory){
        return name;
    }
    function changeName(string memory _name) public{
        name = _name;
    }
}
