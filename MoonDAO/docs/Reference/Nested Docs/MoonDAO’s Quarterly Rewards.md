MoonDAO runs quarterly retroactive rewards every three months at the end of each quarter (Q1 is Jan to Mar, Q2 Apr to Jun, etc). As MoonDAO members, we have the responsibility to review all the projects that were completed over the previous quarter and allocate retroactive rewards to the teams. This process aims to achieve a fair and meritocratic distribution by balancing the recommendations of the Senate with the convictions of all MoonDAO citizens.

## How are the total amount of rewards determined?

Each quarter, both MOONEY and ETH are distributed from the treasury toward completed projects and their contributors.
The amount of ETH released is equal to 5% of the treasury’s total liquid non-MOONEY assets (like ETH, DAI, and other stables).
The amount of MOONEY follows a geometric series where 95% of the amount released in the previous quarter will be distributed in the form of voting power staked for 4 years.

### Example

Throughout this document we’ll use examples from a previous quarter. In this case, the treasury held these liquid assets:

| ASSET | AMOUNT | EXCHANGE RATE | ETH Equivalent |
|-------|--------|---------------|----------------|
| ETH   | 482.38 | 1             | 482.38         |
| WETH  | 0.07   | 0.995         | 0.06           |
| DAI   | 8203.95| 0.0004291     | 3.52           |
| USDT  | 6811.63| 0.0004289     | 2.92           |
| **Total:** | | | **488.89 ETH** |

This brings the total amount of non-MOONEY assets to 488.89 ETH equivalent. If we calculate 5% of this number, we find that the total to be disseminated in this (example) quarter is 24.44 ETH.

Regarding the MOONEY amount, in Q3 2023 there was 12,860,625 MOONEY, so for the following quarter we multiply by 0.95 to find that the Q4 2023 distribution amount is 12,217,593.75 [vMOONEY](vmooney.md). Multiplying that by 0.95 gives 11,606,714 distributed for Q1 2024, etc. The amount released each quarter reduces. Regardless, this amount is locked for four years and is not circulating, cannot be sold during that time, and can only be used for governance and voting.

## How are rewards for each project determined?

The amount per project is determined through a two-step process.

### Step One: Senate Evaluation

As outlined under our Projects system, the senators evaluate each project and suggest a distribution of total rewards (as a percent) that they personally believe should go to each project.

Note: at this stage, senators are prohibited from delegating any value towards projects that they led.

We use a process of iterative normalization to determine the missing values (for projects they led) and anonymize the data prior to the next step. We have also calculated the average of all senator’s distributions.

**![](senate-evaluation-example.png)
### Step Two: Member Vote

This step is the subject of a vote at the beginning of every new quarter. The objective for MoonDAO members is to read the final reports and/or watch the final presentations and vote for the suggested distribution that best reflects their own convictions.

In effect, you are choosing which senator(s) you agree with most and the degree of your support for particular projects, with the average serving as a pseudo-senator. This is your chance to reward projects that you believe had the biggest impact on the DAO.

Each of the projects is represented by an abbreviated code. Please vote on the rocketeer distribution (R1, R2, etc.) that best reflects which projects you think deserve more or fewer rewards, or you can vote for the average from senators. The percentages for each project represent the total that will be awarded to each project.

### Example

This table shows a previous quarter’s senate distribution:

|       | MOTI  | NEWS  | BRID  | SWEE  | ONBO  | NODE  | LIFE  |
|-------|-------|-------|-------|-------|-------|-------|-------|
| **R1**| 7.7%  | 14.44%| 3.72% | 21.18%| 24.07%| 14.44%| 14.44%|
| **R2**| 10%   | 10%   | 5%    | 20%   | 30%   | 10%   | 15%   |
| **R3**| 6.44% | 16.84%| 3.74% | 18.71%| 29%   | 10.29%| 14.97%|
| **R4**| 4.86% | 10.69%| 1.94% | 21.62%| 29.77%| 10.21%| 20.90%|
| **R5**| 4.48% | 17.93%| 4.48% | 22.41%| 31.37%| 10.36%| 8.96% |
| **R6**| 5.16% | 13.98%| 3.44% | 25.81%| 34.41%| 6.88% | 10.32%|
| **AVG**| 6.44%| 13.98%| 3.72% | 21.62%| 29.77%| 10.36%| 14.10%|

For example, if you vote 100% for R3 (Rocketeer 3), it means you support MOTI (MoonDAO in Motion) to receive 6.44% of the total rewards pool, NEWS (Newsletter) to receive 16.84%, etc. If you wanted to provide the most rewards to ONBO (Onboarding Improvement), then you might prefer to vote for R6 (Rocketeer 6) since they suggested 34.41%.

**![](citizen-conviction-results-example.png)

In the example above, Rocketeer 3 (R3) undervalued Project 3 and overvalued Project 1 relative to the other rocketeers. 40% of citizens agree with Rocketeer 3 and this is reflected in the final reward distribution determining what percent of the rewards both MOONEY and non-MOONEY go to each project.

Each project is also typically composed of multiple team members. Each project team internally decides how the total rewards allocated to the project are to be distributed to the team members by percentage, either through a coordinape circle or by other means. This percent value assigned to each team member merits the value of both MOONEY and non-MOONEY assets they receive.

### Example

Using the example quarter’s rewards, if the final value assigned to PROJ1 is 45%, then the project would be awarded 11 ETH (24.44 x 0.45) and 5,497,917.18 MOONEY (12,217,593.75 x 0.45). If Alice, a member on the team, receives 20% of the project's rewards, that means she would receive 2.2 ETH and 1,099,583.436 vMOONEY staked for 4 years for governance votes, minus any in-kind payments received during the course of the project.
