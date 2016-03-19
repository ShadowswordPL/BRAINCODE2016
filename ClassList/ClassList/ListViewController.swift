//
//  ListViewController.swift
//  ClassList
//
//  Created by Tomasz Bąk on 18.03.2016.
//  Copyright © 2016 Za Duzo Tomkow. All rights reserved.
//

import UIKit

class ListViewController: UIViewController {
    @IBOutlet var tableView: UITableView!
    @IBOutlet var info: UILabel!
    @IBOutlet weak var indicator: UIActivityIndicatorView!
    
    var list: [[String]] = [] {
        didSet {
            info.hidden = list.count > 1
            indicator.stopAnimating()
            info.text = "Attendence was not checked"
            tableView.reloadData()
        }
    }

    // MARK: - Table view data source
    @IBAction func photo(sender: UIBarButtonItem) {
        let picker = UIImagePickerController()
        picker.sourceType = .Camera
        picker.delegate = self
        presentViewController(picker, animated: true, completion: nil)
    }
}

extension ListViewController: UIImagePickerControllerDelegate, UINavigationControllerDelegate {
    func imagePickerController(picker: UIImagePickerController, didFinishPickingImage image: UIImage, editingInfo: [String : AnyObject]?) {
        self.dismissViewControllerAnimated(true, completion: nil)
        info.text = "Sending picture..."
        indicator.startAnimating()
        
        sendPicture(image) { [weak self] in
            if let list = $0 {
                self?.list = list
            }
        }
    }
    
    func imagePickerControllerDidCancel(picker: UIImagePickerController) {
        self.dismissViewControllerAnimated(true, completion: nil)
    }
}

extension ListViewController: UITableViewDataSource {
    func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        return list.count
    }
    
    func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return list[section].count
    }
    
    func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCellWithIdentifier("student", forIndexPath: indexPath)
        
        cell.textLabel?.text = list[indexPath.section][indexPath.row]
        
        return cell
    }
    
    func tableView(tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
        return (section == 0) ? "Present" : "Absent"
    }
}

extension ListViewController {
    func sendPicture(picture: UIImage, completion: (list:[[String]]?) -> ()) {
        let url = NSURL(string: "http://10.3.8.65/api/")!
        let request = NSMutableURLRequest(URL: url)
        request.HTTPMethod = "POST"
        let data = UIImageJPEGRepresentation(picture, 1)!
        let base64 = data.base64EncodedStringWithOptions(NSDataBase64EncodingOptions.EncodingEndLineWithLineFeed)
        let json = ["photo": base64]
        request.addValue("application/json", forHTTPHeaderField: "Accept")
        request.addValue("application/json", forHTTPHeaderField: "Content-Type")
        request.HTTPBody = try! NSJSONSerialization.dataWithJSONObject(json, options: NSJSONWritingOptions.PrettyPrinted)
        NSURLSession.sharedSession().dataTaskWithRequest(request) { data, response, error in
            let json = try! NSJSONSerialization.JSONObjectWithData(data!, options: NSJSONReadingOptions(rawValue: 0)) as! [String: AnyObject]
            dispatch_async(dispatch_get_main_queue()) {
                completion(list: [json["present"] as! [String], json["absent"] as! [String]])
            }
        }.resume()
    }
}
