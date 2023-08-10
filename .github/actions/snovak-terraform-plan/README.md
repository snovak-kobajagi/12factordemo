# Intro

- Required: <https://aws.amazon.com/architecture/well-architected/>

- Harden Github workflow config: <https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services>

## Credentials

We recommend following
[Amazon IAM best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
for the AWS credentials used in GitHub Actions workflows, including:

- Do not store credentials in your repository's code.
- [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) to the credentials used in GitHub Actions
  workflows. Grant only the permissions required to perform the actions in your
  GitHub Actions workflows.
- [Monitor the activity](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#keep-a-log) of the credentials used in GitHub Actions workflows.

## Assuming a Role

There are four different supported ways to retrieve credentials. We recommend
using [GitHub's OIDC provider](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services)
to get short-lived credentials needed for your actions. Specifying
`role-to-assume` **without** providing an `aws-access-key-id` or a
`web-identity-token-file`, or setting `role-chaining`, will signal to the action that you wish to use the
OIDC provider. If `role-chaining` is `true`, existing credentials in the environment will be used to assume `role-to-assume`.

The following table describes which identity is used based on which values are supplied to the Action:

| **Identity Used**                                               | `aws-access-key-id` | `role-to-assume` | `web-identity-token-file` | `role-chaining` |
| --------------------------------------------------------------- | ------------------- | ---------------- | ------------------------- | - |
| [✅ Recommended] Assume Role directly using GitHub OIDC provider |                     | ✔                |                           | |
| IAM User                                                        | ✔                   |                  |                           | |
| Assume Role using IAM User credentials                          | ✔                   | ✔                |                           | |
| Assume Role using WebIdentity Token File credentials            |                     | ✔                | ✔                         | |
| Assume Role using existing credentials | | ✔ | | ✔ |

### Credential Lifetime

The default session duration is **1 hour** when using the OIDC provider to
directly assume an IAM Role or when an `aws-session-token` is directly provided.
The default session duration is **6 hours** when using an IAM User to assume an
IAM Role (by providing an `aws-access-key-id`, `aws-secret-access-key`, and a
`role-to-assume`) .
