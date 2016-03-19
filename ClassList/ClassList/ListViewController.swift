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
    var dataTask: NSURLSessionDataTask?
    
    var list: [[String]] = [] {
        didSet {
            info.hidden = list.count > 1
            info.text = "Attendence was not checked"
            tableView.reloadData()
        }
    }
    
    override func didMoveToParentViewController(parent: UIViewController?) {
        if parent == nil {
            dataTask?.cancel()
        }
    }

    // MARK: - Table view data source
    @IBAction func photo(sender: UIBarButtonItem) {
        let picker = UIImagePickerController()
        picker.sourceType = .Camera//.PhotoLibrary
        picker.delegate = self
        presentViewController(picker, animated: true, completion: nil)
    }
}

extension ListViewController: UIImagePickerControllerDelegate, UINavigationControllerDelegate {
    func imagePickerController(picker: UIImagePickerController, didFinishPickingImage image: UIImage, editingInfo: [String : AnyObject]?) {
        self.dismissViewControllerAnimated(true, completion: nil)
        list = []
        info.text = "Sending picture..."
        indicator.startAnimating()
        
        sendPicture(image.rotateImageByOrientation()) { [weak self] in
            if let list = $0 {
                self?.indicator.stopAnimating()
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
        guard let url = NSURL(string: "http://\(DevViewController.address)/api/"), data = UIImageJPEGRepresentation(picture, 1) else {
            info.text = "error"
            return
        }
        
        let request = NSMutableURLRequest(URL: url)
        request.HTTPMethod = "POST"
        let base64 = data.base64EncodedStringWithOptions(NSDataBase64EncodingOptions.EncodingEndLineWithLineFeed)
        let json = ["photo": base64]
        request.addValue("application/json", forHTTPHeaderField: "Accept")
        request.addValue("application/json", forHTTPHeaderField: "Content-Type")
        request.HTTPBody = try! NSJSONSerialization.dataWithJSONObject(json, options: NSJSONWritingOptions.PrettyPrinted)
        dataTask = NSURLSession.sharedSession().dataTaskWithRequest(request) { [weak self] data, response, error in
            if let _ = error {
                self?.info.text = "error"
            }
            
            guard let json = try? NSJSONSerialization.JSONObjectWithData(data!, options: NSJSONReadingOptions(rawValue: 0)),
                let array = json as? [String: AnyObject],
                let present = array["present"] as? [String],
                let absent = array["absent"] as? [String] else {
                self?.info.text = "error"
                return
            }
            dispatch_async(dispatch_get_main_queue()) {
                completion(list: [present, absent])
            }
        }
        
        dataTask?.resume()
    }
}

// Source: http://stackoverflow.com/a/33479054/2777364
extension UIImage {
    func rotateImageByOrientation() -> UIImage {
        // No-op if the orientation is already correct
        guard self.imageOrientation != .Up else {
            return self
        }
        
        // We need to calculate the proper transformation to make the image upright.
        // We do it in 2 steps: Rotate if Left/Right/Down, and then flip if Mirrored.
        var transform = CGAffineTransformIdentity;
        
        switch (self.imageOrientation) {
        case .Down, .DownMirrored:
            transform = CGAffineTransformTranslate(transform, self.size.width, self.size.height)
            transform = CGAffineTransformRotate(transform, CGFloat(M_PI))
            
        case .Left, .LeftMirrored:
            transform = CGAffineTransformTranslate(transform, self.size.width, 0)
            transform = CGAffineTransformRotate(transform, CGFloat(M_PI_2))
            
        case .Right, .RightMirrored:
            transform = CGAffineTransformTranslate(transform, 0, self.size.height)
            transform = CGAffineTransformRotate(transform, CGFloat(-M_PI_2))
            
        default:
            break
        }
        
        switch (self.imageOrientation) {
        case .UpMirrored, .DownMirrored:
            transform = CGAffineTransformTranslate(transform, self.size.width, 0)
            transform = CGAffineTransformScale(transform, -1, 1)
            
        case .LeftMirrored, .RightMirrored:
            transform = CGAffineTransformTranslate(transform, self.size.height, 0)
            transform = CGAffineTransformScale(transform, -1, 1)
            
        default:
            break
        }
        
        // Now we draw the underlying CGImage into a new context, applying the transform
        // calculated above.
        let ctx = CGBitmapContextCreate(nil, Int(self.size.width), Int(self.size.height),
            CGImageGetBitsPerComponent(self.CGImage), 0,
            CGImageGetColorSpace(self.CGImage),
            CGImageGetBitmapInfo(self.CGImage).rawValue)
        CGContextConcatCTM(ctx, transform)
        switch (self.imageOrientation) {
        case .Left, .LeftMirrored, .Right, .RightMirrored:
            CGContextDrawImage(ctx, CGRectMake(0,0,self.size.height,self.size.width), self.CGImage)
            
        default:
            CGContextDrawImage(ctx, CGRectMake(0,0,self.size.width,self.size.height), self.CGImage)
        }
        
        // And now we just create a new UIImage from the drawing context
        if let cgImage = CGBitmapContextCreateImage(ctx) {
            return UIImage(CGImage: cgImage)
        } else {
            return self
        }
    }
}
