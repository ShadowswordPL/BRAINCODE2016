//
//  ClassesViewController.swift
//  ClassList
//
//  Created by Tomasz Bąk on 19.03.2016.
//  Copyright © 2016 Za Duzo Tomkow. All rights reserved.
//

import UIKit

class ClassesViewController: UITableViewController {
    let classes = ["6A", "6B", "6C", "6D"]
    
    override func viewWillAppear(animated: Bool) {
        navigationController?.navigationBarHidden = false
    }

    override func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        return 1
    }

    override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return classes.count
    }

    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCellWithIdentifier("class", forIndexPath: indexPath)

        cell.textLabel?.text = classes[indexPath.row]

        return cell
    }
}
