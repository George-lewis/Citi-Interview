// A Rust implementation of `comments.py`
// Written on my own time

use itertools::Itertools;

fn main() {
    let filename = std::env::args().nth(1).expect("Please provide a filename");
    let data = std::fs::read_to_string(filename).expect("Failed to read file");

    let mut start = None;
    let mut segments = vec![0];

    // Safety: We assume the input file is ASCII
    // In Rust strings are UTF-8, which makes iterating over them a bit more tedious
    // So this assumption simplifies the implemention, and is in fact implicitly made in Python
    let windows = data.as_bytes().iter().enumerate().tuple_windows();

    // Windows are a nice abstraction
    for ((i, &a), (_, &b)) in windows {
        match (start, a, b) {
            (_, b'/', b'*') => {
                start = Some(i);
            }
            (Some(start_), b'*', b'/') => {
                segments.extend([start_, i + 2]);
                start = None;
            }
            _ => { /* no-op */ }
        }
    }

    segments.push(data.as_bytes().len());

    let mut new_string = String::new();

    // Non-overlapping - this vec is always an even length
    // Invert the mask
    for (&start, &end) in segments.iter().tuples() {
        new_string.push_str(&data[start..end]);
    }

    println!("{}", &new_string);
}
