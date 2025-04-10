# ERC-3525: Semi-Fungible Token

## About the Project

This repository contains a formal verification of ERC-3525 using **Certora**. Our goal with this project is to take a step further, given that we already took the first step with the ERC-4337 project. However, we encountered some issues when applying tests with ERC-4337, which are mentioned in that repository. If you're interested in reading about it, [click here.](https://github.com/phdfreitas/erc4337-account-abstraction)

With this project involving Certora, beyond the goal mentioned above, we also want to test Certora on a real contract and gain some hands-on experience with this tool. This will allow us to see the advantages and disadvantages of using Certora compared to other tools like Halmos, despite the different application contexts.

## ERC-3525

Speaking a little bit about the contract we applied formal verification to, it introduces the concept of _semi-fungible tokens_. In this case, it combines properties from both ERC-20 and ERC-721. To learn more, [click here.](https://eips.ethereum.org/EIPS/eip-3525)

## Certora

As mentioned earlier, Certora is a tool that allows formal verification of smart contracts. It enables you to write formal specifications using _rules, invariants, and ghost variables_. This allows us to verify contract behavior without needing to run traditional tests.

## About the Project Development

To run tests on ERC-3525, we initially tried to download the contract using **forge install**. However, when writing the _rules_, we encountered several issues. After that attempt, we downloaded the contract implementation itself (available [here]) along with its required dependencies. Yet again, we faced many problems while executing the _spec_ file. The main issue was related to accessing more than one directory for rule execution. That is, at first, the contract was placed in the **src folder** and its dependencies (as expected) were in the **lib folder**. However, even after configuring the **.conf** file to allow Certora access to both directories, some exceptions were thrown during "compilation" due to this issue.

After some research, it seems that Certora can only access the directory where the .spec file is located plus one additional directory **(set via solc_allow_path).**

To handle this problem, we initialized a new Foundry project (**forge init**), created a **certora > conf** folder, and inside it we placed both the contract implementation and its dependencies. We understand this may not be the ideal approach, but it was the solution we found to make it work, at least at the time of writing this. It may change in the future.

## About the Tests (spec/rules)

Our initial goal with the tests was to focus mainly on the 'public' methods defined in the ERC-3525 interface. In this sense, we created rules for the following methods:

- [x] balanceOf
- [x] slotOf
- [x] approve
- [x] allowance
- [x] transferFrom

## Tests/Rules

- [x] test_name: test description
- [x] transferValuePreservesTotal: Verifies that value transfers between tokens of the same slot maintain total balance integrity (sum of values before/after must be equal).
- [x] mintOnTransferIncreasesSupply: Confirms that transfers to a new address create a derived token and increment totalSupply.
- [x] derivedTokenInheritsSlot:Validates that tokens created via transfer inherit the original token’s slot.
- [x] transferToZeroAddressFails: Checks that transfers to address(0) revert, preventing accidental token burns.
- [x] approveZeroAddressFails: Ensures approvals for address(0) revert, blocking invalid authorizations.
- [x] concurrentApprovalChange: Tests whether concurrent allowance changes (approve + revoke) leave no inconsistent state.

Some rules were mentioned above. With them, our goal was to test some possible scenarios we identified and considered interesting, at least as a starting point. In this sense, we believe we achieved a satisfactory initial result. From now on, however, a deeper study of both ERC-3525 and Certora will be necessary in order to create more complex and refined scenarios.

## Results

In general, our *tests* passed. However, if you check the **"FinalResults.html"** file, you’ll notice that two of them resulted in a "Sanity check failed" status. In other words, Certora did not find a valid execution for them. We’ll revisit this later. For now, our focus is on writing some rules and invariants so we can perform a more in-depth analysis of each one later on.

Another point worth mentioning is that one of our tests fails. Although the logic of the test seems correct, Certora generates two different values for what should be equal during execution. Due to our current lack of knowledge, we haven't been able to make those values match without "forcing" them, i.e, assigning the value directly. Still, we found it interesting that one of our own mistakes could lead to incorrect conclusions, so we decided to keep this test/rule in the specification and mention it here.

Just out of curiosity, we are referring to the following rule: *onlyAuthorizedCanTransferSpec*.

So far, this is the work we’ve done.
