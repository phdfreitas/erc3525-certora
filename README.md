# ERC-3525: Semi-Fungible Token

## About the Project
This repository contains a formal verification of ERC-3525 using **Certora**. Our goal with this project is to take a step further, given that we already took the first step with the ERC-4337 project. However, we encountered some issues when applying tests with ERC-4337, which are mentioned in that repository — if you're interested in reading about it, click here.

With this project involving Certora, beyond the goal mentioned above, we also want to test Certora on a real contract and gain some hands-on experience with this tool. This will allow us to see the advantages and disadvantages of using Certora compared to other tools like Halmos, despite the different application contexts.

## ERC-3525
Speaking a little bit about the contract we applied formal verification to, it introduces the concept of *semi-fungible tokens*. In this case, it combines properties from both ERC-20 and ERC-721. To learn more, click here.

## Certora
As mentioned earlier, Certora is a tool that allows formal verification of smart contracts. It enables you to write formal specifications using *rules, invariants, and ghost variables*. This allows us to verify contract behavior without needing to run traditional tests.

## About the Project Development
To run tests on ERC-3525, we initially tried to download the contract using **forge install**. However, when writing the *rules*, we encountered several issues. After that attempt, we downloaded the contract implementation itself (available [here]) along with its required dependencies. Yet again, we faced many problems while executing the *spec* file. The main issue was related to accessing more than one directory for rule execution. That is, at first, the contract was placed in the **src folder** and its dependencies (as expected) were in the **lib folder**. However, even after configuring the **.conf** file to allow Certora access to both directories, some exceptions were thrown during "compilation" due to this issue.

After some research, it seems that Certora can only access the directory where the .spec file is located plus one additional directory **(set via solc_allow_path).**

To handle this problem, we initialized a new Foundry project (**forge init**), created a **certora > conf** folder, and inside it we placed both the contract implementation and its dependencies. We understand this may not be the ideal approach, but it was the solution we found to make it work — at least at the time of writing this. It may change in the future.

## About the Tests (spec/rules)
Our initial goal with the tests was to focus mainly on the 'public' methods defined in the ERC-3525 interface. In this sense, we created rules for the following methods:

- [x] balanceOf
- [x] slotOf
- [x] approve
- [x] allowance
- [x] transferFrom

## Tests/Rules
