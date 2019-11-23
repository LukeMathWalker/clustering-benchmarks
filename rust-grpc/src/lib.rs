pub mod server;

use std::path::PathBuf;
use linfa_clustering::KMeans;

pub struct Store {
    pub kmeans: KMeans,
}

impl Store {
    pub fn load(path: PathBuf) -> Result<Self, anyhow::Error> {
        let reader = std::fs::File::open(path)?;
        Ok(Self {
            kmeans: serde_json::from_reader(reader)?,
        })
    }
}

#[cfg(test)]
mod test {
    use super::*;
    use ndarray::{s, array, ArrayView2};


    #[test]
    fn load_from_file() {
        Store::load("../data/rust_k_means_model.json".into()).expect("failed to load from input file");
    }


    #[test]
    fn integration() {
        let store = Store::load("../data/rust_k_means_model.json".into())
            .expect("failed to load from input file");

        let sl = s![0..1, ..];
        let observations: ArrayView2<f64> = 
            store.kmeans.centroids().unwrap().slice(sl);
        assert_eq!(
            store.kmeans.predict(&observations),
            array![0]
        );
    }
}
