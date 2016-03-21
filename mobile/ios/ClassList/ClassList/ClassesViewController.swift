//
//  ClassesViewController.swift
//  ClassList
//
//  Created by Tomasz Bąk on 19.03.2016.
//  Copyright © 2016 Za Duzo Tomkow. All rights reserved.
//

import UIKit

class ClassesViewController: UIViewController, UITableViewDataSource {
    let classes = ["6A - mathematics", "6B - mathematics", "6C - mathematics", "6D - mathematics"]
    let hours = ["2016-03-19 10:00", "2016-03-19 11:00", "2016-03-19 12:00", "2016-03-19 13:00"]
    @IBOutlet var tableView: UITableView!
    
    override func viewWillAppear(animated: Bool) {
        navigationController?.navigationBarHidden = false
    }

    func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        return 1
    }

    func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return classes.count
    }

    func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCellWithIdentifier("class", forIndexPath: indexPath)

        cell.textLabel?.text = classes[indexPath.row]
        cell.detailTextLabel?.text = hours[indexPath.row]

        return cell
    }
}
