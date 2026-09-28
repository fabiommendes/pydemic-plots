from invoke import task


@task
def prepare_data(ctx, demography=True, summary=True):
    args = ' '.join(f'--{k}' for k, v in locals().items() if v is True)
    ctx.run(f"python -m mundi_ibge.prepare {args}", pty=True)


@task
def test(ctx):
    ctx.run("pytest tests/ --cov")
    ctx.run("black --check .")
    ctx.run("pycodestyle")
