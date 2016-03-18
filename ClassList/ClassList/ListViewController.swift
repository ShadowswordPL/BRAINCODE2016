//
//  ListViewController.swift
//  ClassList
//
//  Created by Tomasz Bąk on 18.03.2016.
//  Copyright © 2016 Za Duzo Tomkow. All rights reserved.
//

import UIKit

class ListViewController: UITableViewController {
    let list = [["Jan Kowalski", "Janina Kowalska", "Stefan Alegor"], ["Krzysztof Jarzyna", "Patryk Bakłażan"]]

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    // MARK: - Table view data source

    override func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        return list.count
    }

    override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return list[section].count
    }

    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCellWithIdentifier("person", forIndexPath: indexPath)

        cell.textLabel?.text = list[indexPath.section][indexPath.row]

        return cell
    }
    
    override func tableView(tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
        return (section == 0) ? "Present" : "Absent"
    }
}
