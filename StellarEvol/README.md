## Setting up the Repository

1. Go to https://github.com/RoryBarnes/LP890-9 

2. Fork the most recent version of the code (make sure to unselect copy on main branch)

3. On your local machine in a desired directory, clone the repo 
```
git clone https://github.com/jbirky/LP890-9.git 
cd LP890-9/StellarEvol
```

4. Within the `LP890-9/StellarEvol directory`, copy the template jupyter notebook to a directory called your git username 
```
cp -r template <username>
```

5. Launch jupyter notebook and navigate to `LP890-9/StellarEvol/username/run_stellar.ipynb`

## Uploading Results to Github

1. We will make all of our commits to the `stellar` branch
```
	git checkout stellar
```

2. After you’ve made code modifications / have simulations to upload, add and commit them to git 
```
	git add <username>/run_stellar.ipynb
	git add <username>/simulations.npz
	git commit -m “upload results”
	git push origin stellar
```
Add any other results you want to contribute, but make sure not to upload files more than 100MB! 

3. On github, navigate back to your forked branch https://github.com/jbirky/LP890-9. At the top of the repo click ‘contribute’ to create a pull request. One of the admins will then merge your contributions to the main repository.


