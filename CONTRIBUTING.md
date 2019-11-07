# How to contribute

We definitely welcome your patches and contributions to conan-grpc!

If you are new to github, please start by reading [Pull Request
howto](https://help.github.com/articles/about-pull-requests/)

## Testing the package

When editing the Conan package, it is convenient to use the following commands to test each package
creation step:
```
conan source . --source-folder=tmp/source
conan install . --install-folder=tmp/source
conan build . --source-folder=tmp/source --build-folder=tmp/source --package-folder=tmp/package
conan package . --source-folder=tmp/source --build-folder=tmp/source --package-folder=tmp/package
conan export-pkg . osechet/testing --package-folder=tmp/package -f
conan test test_package gRPC/1.25.0@osechet/testing
```

## Creating the package

Once the package has been tested, it is possible to create it using the
`conan create . osechet/testing` command.

The official package creation is managed in CI/CD using the
[conan_package_tools](https://docs.conan.io/en/latest/creating_packages/package_tools.html).

## Guidelines for Pull Requests
How to get your contributions merged smoothly and quickly.

- Create **small PRs** that are narrowly focused on **addressing a single
  concern**.  We often times receive PRs that are trying to fix several things
  at a time, but only one fix is considered acceptable, nothing gets merged and
  both author's & review's time is wasted.  Create more PRs to address different
  concerns and everyone will be happy.

- For speculative changes, consider opening an issue and discussing it first.

- Provide a good **PR description** as a record of **what** change is being made
  and **why** it was made.  Link to a GitHub issue if it exists.

- Don't fix code style and formatting unless you are already changing that line
  to address an issue.  PRs with irrelevant changes won't be merged.  If you do
  want to fix formatting or style, do that in a separate PR.

- Unless your PR is trivial, you should expect there will be reviewer comments
  that you'll need to address before merging.  We expect you to be reasonably
  responsive to those comments, otherwise the PR will be closed after 2-3 weeks
  of inactivity.

- Maintain **clean commit history** and use **meaningful commit messages**.
  PRs with messy commit history are difficult to review and won't be merged.
  Use `rebase -i upstream/master` to curate your commit history and/or to
  bring in latest changes from master (but avoid rebasing in the middle of
  a code review).

- Keep your PR up to date with upstream/master (if there are merge conflicts,
  we can't really merge your change).

- **All tests need to be passing** before your change can be merged.

- Exceptions to the rules can be made if there's a compelling reason for doing
  so.
